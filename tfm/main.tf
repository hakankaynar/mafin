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
  name = "mafin_ecs_log_group"
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