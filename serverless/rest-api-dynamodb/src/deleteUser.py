import json
import boto3

def deleteUser(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('rest-api-dynamodb-dev')

    userId = event['userId']

    table.delete_item(
        Key={
            'userId': userId
        }
    )

    body = {
        "message": "User deleted!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
