import boto3
import zipfile
import os

lambda_client = boto3.client('lambda')

# Step 1: Zip the function
def create_zip():
    with zipfile.ZipFile('function.zip', 'w') as zipf:
        zipf.write('lambda_function.py')

# Step 2: Create Lambda function
def create_lambda():
    role_arn = 'arn:aws:iam::231299271232:role/lambda-execution-role'
    with open('function.zip', 'rb') as f:
        zipped_code = f.read()

    response = lambda_client.create_function(
        FunctionName='MyAutomatedLambda',
        Runtime='python3.12',
        Role=role_arn,
        Handler='lambda_function.lambda_handler',
        Code=dict(ZipFile=zipped_code),
        Timeout=15,
        MemorySize=128,
        Publish=True
    )
    print("✅ Lambda function created!")
    print("Lambda ARN:", response['FunctionArn'])

if __name__ == '__main__':
    create_zip()
    create_lambda()
 
