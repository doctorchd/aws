#!/usr/bin/env bash

#!/bin/bash

aws s3 rm s3://lohika-s3-bucket --recursive

aws cloudformation delete-stack --stack-name TestVPC
