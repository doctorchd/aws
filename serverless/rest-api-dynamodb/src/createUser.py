import json
import boto3

def createUser(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('rest-api-dynamodb-dev')

    request_data = json.loads(event["body"])
    userId = request_data['userId']
    firstName = request_data['firstName']
    lastName = request_data['lastName']
    userName = request_data['userName']

    table.put_item(
        Item={
            'userId': userId,
            'firstName': firstName,
            'lastName': lastName,
            'userName': userName
        }
    )

    body = {
        "message": "User created!",
        # "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
