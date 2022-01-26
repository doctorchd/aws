import json
import boto3


def s3processor(event, context):
    sqs = boto3.resource('sqs')
    
    for queue in sqs.queues.all():
        print(queue.url)
    
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
