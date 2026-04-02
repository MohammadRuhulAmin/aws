import json
def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps({
            'event': event,    
            'requestId': context.aws_request_id,
            'function': context.function_name
        }),
        'headers': {
            'Content-Type': 'application/json'
        }
    }

"""
    {
        "event": {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/",
            "rawQueryString": "name=Ruhul",
            "headers": {
                "content-length": "0",
                "x-amzn-tls-version": "TLSv1.3",
                "x-forwarded-proto": "https",
                "postman-token": "e797da55-5202-42ec-9022-2859c1fecb70",
                "x-forwarded-port": "443",
                "x-forwarded-for": "202.5.62.75",
                "accept": "*/*",
                "x-amzn-tls-cipher-suite": "TLS_AES_128_GCM_SHA256",
                "x-amzn-trace-id": "Self=1-69ce31a0-715f7c1a1b90e2a76fbbb834;Root=1-69ce31a0-38502a633a55086f005d772f",
                "host": "7z5qxazz4jo7fp5jbbnue4xhxi0arzqq.lambda-url.us-east-1.on.aws",
                "cache-control": "no-cache",
                "accept-encoding": "gzip, deflate, br",
                "user-agent": "PostmanRuntime/7.52.0"
            },
            "queryStringParameters": {
                "name": "Ruhul"
            },
            "requestContext": {
                "accountId": "anonymous",
                "apiId": "7z5qxazz4jo7fp5jbbnue4xhxi0arzqq",
                "domainName": "7z5qxazz4jo7fp5jbbnue4xhxi0arzqq.lambda-url.us-east-1.on.aws",
                "domainPrefix": "7z5qxazz4jo7fp5jbbnue4xhxi0arzqq",
                "http": {
                    "method": "GET",
                    "path": "/",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "202.5.62.75",
                    "userAgent": "PostmanRuntime/7.52.0"
                },
                "requestId": "3b594a9a-be8d-4137-b497-b2f10b5b50e2",
                "routeKey": "$default",
                "stage": "$default",
                "time": "02/Apr/2026:09:06:40 +0000",
                "timeEpoch": 1775120800140
            },
            "isBase64Encoded": false
        },
        "requestId": "3b594a9a-be8d-4137-b497-b2f10b5b50e2",
        "function": "data_extraction"
    }    
    
"""