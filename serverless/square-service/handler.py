import json


def square(event, context):
    
    length = event['length']
    width = event['width']

    square_value = length * width

    response = {
        "statusCode": 200,
        "body": json.dumps(square_value)
    }

    return response
