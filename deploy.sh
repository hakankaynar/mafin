#!/bin/bash

cd app
docker build -t mafin .

docker tag mafin 518455494753.dkr.ecr.us-east-1.amazonaws.com/mafin_ecr:0.0.11
docker push 518455494753.dkr.ecr.us-east-1.amazonaws.com/mafin_ecr:0.0.11

docker tag mafin 518455494753.dkr.ecr.us-east-1.amazonaws.com/mafin_ecr:latest
docker push 518455494753.dkr.ecr.us-east-1.amazonaws.com/mafin_ecr:latest