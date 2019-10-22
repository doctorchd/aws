#!/bin/bash

# upload files to s3
for file in ~/files/*; do
    aws s3 cp $file s3://lohika-s3-bucket
done
