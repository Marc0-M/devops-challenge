import json
import os
import boto3
dynamodb = boto3.resource('dynamodb')


def list(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch all Usernames from the database
    result = table.scan()

    method = event['httpMethod']
    headers = json.dumps(event['headers'])


    # create a response
    response = {
        "statusCode": 200,
        "body": 'Welcome to our demo API, here are the details of your request: \n \n' + 'Headers: \n \n' + headers + '\n \nMethod: \n \n' + json.dumps(method) + '\n \nBody: \n' +json.dumps(result)
    }

    return response