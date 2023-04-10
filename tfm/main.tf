terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
}

resource "aws_ecr_repository" "mafin_ecr" {
  name                 = "mafin_ecr"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}

data "aws_iam_policy_document" "mafin_ecr_policy" {
  statement {
    sid    = "new policy"
    effect = "Allow"

    principals {
      type        = "*"
      identifiers = ["*"]
    }

    actions = [
      "ecr:GetDownloadUrlForLayer",
      "ecr:BatchGetImage",
      "ecr:BatchCheckLayerAvailability",
      "ecr:PutImage",
      "ecr:InitiateLayerUpload",
      "ecr:UploadLayerPart",
      "ecr:CompleteLayerUpload",
      "ecr:DescribeRepositories",
      "ecr:GetRepositoryPolicy",
      "ecr:ListImages",
      "ecr:DeleteRepository",
      "ecr:BatchDeleteImage",
      "ecr:SetRepositoryPolicy",
      "ecr:DeleteRepositoryPolicy",
    ]
  }
}

resource "aws_ecr_repository_policy" "mafin_ecr_policy" {
  repository = aws_ecr_repository.mafin_ecr.name
  policy     = data.aws_iam_policy_document.mafin_ecr_policy.json
}




resource "aws_kms_key" "mafin_kms_key" {
  description             = "mafin"
  deletion_window_in_days = 7
}

resource "aws_cloudwatch_log_group" "mafin_ecs_log_group" {
  name = "mafin"
}

resource "aws_ecs_cluster" "mafin_ecs_cluster" {
  name = "mafin_ecs_cluster"

  configuration {
    execute_command_configuration {
      kms_key_id = aws_kms_key.mafin_kms_key.arn
      logging    = "OVERRIDE"

      log_configuration {
        cloud_watch_encryption_enabled = true
        cloud_watch_log_group_name     = aws_cloudwatch_log_group.mafin_ecs_log_group.name
      }
    }
  }
}


resource "aws_ecs_cluster_capacity_providers" "mafin_ecs_cap_provider" {
  cluster_name = aws_ecs_cluster.mafin_ecs_cluster.name

  capacity_providers = ["FARGATE"]

  default_capacity_provider_strategy {
    base              = 1
    weight            = 100
    capacity_provider = "FARGATE"
  }
}

resource "aws_iam_role" "ecs_task_execution_role" {
  name = "ecs_task_execution_role"

  # Terraform's "jsonencode" function converts a
  # Terraform expression result to valid JSON syntax.
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid: "",
        Effect: "Allow",
        Principal: {
            Service: "ecs-tasks.amazonaws.com"
        },
        Action: "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_role_policy" "log_policy" {
  name = "log_policy"
  role = aws_iam_role.ecs_task_execution_role.id

  # Terraform's "jsonencode" function converts a
  # Terraform expression result to valid JSON syntax.
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect: "Allow",
        Action: [
            "ecr:GetAuthorizationToken",
            "ecr:BatchCheckLayerAvailability",
            "ecr:GetDownloadUrlForLayer",
            "ecr:BatchGetImage",
            "logs:CreateLogStream",
            "logs:PutLogEvents"
        ],
        Resource: "*"
      },
    ]
  })
}

resource "aws_iam_role_policy" "ses_policy" {
  name = "ses_policy"
  role = aws_iam_role.ecs_task_execution_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action: [
          "ses:SendEmail",
          "ses:SendRawEmail"
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}



resource "aws_ecs_task_definition" "mafin_task" {
  family = "mafin"
  cpu       = 256
  memory    = 1024
  requires_compatibilities = ["FARGATE"]
  container_definitions = file("container_definition.json")
  network_mode = "awsvpc"
  execution_role_arn = aws_iam_role.ecs_task_execution_role.arn

  ephemeral_storage {
    size_in_gib = 21
  }
}