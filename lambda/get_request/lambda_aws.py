import json

def lambda_handler(event, context):
    json_content = {
        'statusCode': 200,
        'headers': {
            'envType': 'aws',
            'about': 'test'
        },
        'body': json.dumps({
            'data': 'Hello from Lambda!',
            'uuid': '12233'
        })
    }
    return json_content