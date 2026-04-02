Context is a runtime information object of AWS Lambda Function.

```sh
context.function_name
context.function_version
context.aws_request_id
context.get_remaining_time_in_millis()
context.memory_limit_in_mb

def lambda_handler(event, context):
    print("Function:", context.function_name)
    print("Request ID:", context.aws_request_id)
    print("Time left (ms):", context.get_remaining_time_in_millis())

    return {
        'statusCode': 200,
        'body': 'Check logs'
    }
```