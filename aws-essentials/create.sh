#!/usr/bin/env bash

aws cloudformation create-stack --stack-name TestVPC --template-body file://TestVPC.json