import json
import boto3

def createUser(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('rest-api-dynamodb-dev')

    userId = event['userId']
    userName = event['userName']
    firstName = event['firstName']
    lastName = event['lastName']

    table.put_item(
        Item={
            'userId': userId,
            'userName': userName,
            'firstName': firstName,
            'lastName': lastName
        }
    )

    body = {
        "message": "User created!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
