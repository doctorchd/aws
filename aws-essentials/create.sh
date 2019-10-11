#!/usr/bin/env bash

if [ "XXX$1" = "XXX" ]; then
    echo "Add VPC name as parameter"
    echo
    exit 1
fi

TMPL="$1"

if [ ! -f $TMPL ]; then
    echo "File $TMPL does not exist"
    exit 1
fi

aws cloudformation create-stack \
    --stack-name TestVPC \
    --template-body file://$TMPL \
    --capabilities CAPABILITY_NAMED_IAM

