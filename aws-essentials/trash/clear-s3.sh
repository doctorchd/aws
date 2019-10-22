#!/bin/bash

for file in \
    `aws s3 ls s3://lohika-s3-bucket | \
     sed "s/  */ /g" | cut -d " " -f 4`; do

    aws s3 rm s3://lohika-s3-bucket/$file
done
