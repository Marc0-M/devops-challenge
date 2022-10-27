import json
import logging
import os

import boto3
dynamodb = boto3.resource('dynamodb')


def create(event, context):
    data = json.loads(event['body'])
    if 'username' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item.")

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'username': data['username'],
        'password': data['password']
    }

    # write the todo to the database
    table.put_item(Item=item)

    method = event['httpMethod']
    headers = json.dumps(event['headers'])


    # create a response
    response = {
        "statusCode": 200,
        "body": 'Welcome to our demo API, here are the details of your request: \n \n' + 'Headers: \n \n' + headers + '\n \nMethod: \n \n' + json.dumps(method) + '\n \nBody: \n' +json.dumps(item)
    }

    return response