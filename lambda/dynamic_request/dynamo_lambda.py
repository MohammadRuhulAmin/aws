import json 

def lambda_handler(event, context):
    method = event.get('httpMethod')

    if method == 'POST':
        body = json.loads(event.get('body', '{}'))
        return {
            'statusCode': 200,
            'body': json.dumps(body)
        }

    elif method == 'GET':
        params = event.get('queryStringParameters') or {}
        return {
            'statusCode': 200,
            'body': json.dumps(params)
        }