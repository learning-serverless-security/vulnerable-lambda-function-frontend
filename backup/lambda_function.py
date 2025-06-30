from os import environ
get_env = environ.get

HARDCODED_CREDENTIAL_01 = "ABCDE"
HARDCODED_CREDENTIAL_02 = "FGHIJ"


def get_statement(event):
    params = event.get('queryStringParameters', {})
    statement = params.get('statement', None)
    
    return statement


def process_statement(statement):
    output = "No statement parameter value provided"
    
    if statement:
        output = eval(statement)
    
    return output


def lambda_handler(event, context):
    print("event: ", event)
    print("HARDCODED_CREDENTIAL_01: ", HARDCODED_CREDENTIAL_01)
    print("HARDCODED_CREDENTIAL_02: ", HARDCODED_CREDENTIAL_02)
    print("CUSTOM_ENV_VAR_01: ", get_env('CUSTOM_ENV_VAR_01'))
    print("CUSTOM_ENV_VAR_02: ", get_env('CUSTOM_ENV_VAR_02'))
    
    statement = get_statement(event)
    result = process_statement(statement)
    
    return {
        'statusCode': 200,
        'body': str(result)
    }
