#!/usr/bin/env bash

aws cloudformation create-stack \
    --stack-name TestVPC \
    --template-body file://VPC.json \
    --capabilities CAPABILITY_NAMED_IAM
