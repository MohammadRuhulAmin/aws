import json

def lambda_handler(event, context):
    params = event.get('queryStringParameters') or {}
    name = params.get('name', 'default_user')
    return {
        'statusCode': 200,
        'headers': {
            'envType': 'aws',
            'about': 'test'
        },
        'body': json.dumps({
            'data': f'Hello {name}!',
            'uuid': '12233'
        })
    }