import json
import boto3

def getUser(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('rest-api-dynamodb-dev')

    userId = event['userId']

    response = table.get_item(
        Key={
            'userId': userId
        }
    )
    item = response['Item']

    body = {
        "message": "User exists!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
