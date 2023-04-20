#!/bin/bash
VERSION="${1:-0.0.28}"

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 518455494753.dkr.ecr.us-east-1.amazonaws.com

cd app
docker build -t mafin .

docker tag mafin 518455494753.dkr.ecr.us-east-1.amazonaws.com/mafin_ecr:$VERSION
docker push 518455494753.dkr.ecr.us-east-1.amazonaws.com/mafin_ecr:$VERSION

docker tag mafin 518455494753.dkr.ecr.us-east-1.amazonaws.com/mafin_ecr:latest
docker push 518455494753.dkr.ecr.us-east-1.amazonaws.com/mafin_ecr:latest