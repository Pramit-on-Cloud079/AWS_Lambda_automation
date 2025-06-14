import boto3
import json

iam = boto3.client('iam')

role_name = "lambda-execution-role"

assume_role_policy = {
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Principal": {"Service": "lambda.amazonaws.com"},
        "Action": "sts:AssumeRole"
    }]
}

# Step 1: Create Role
response = iam.create_role(
    RoleName=role_name,
    AssumeRolePolicyDocument=json.dumps(assume_role_policy),
    Description="IAM role for Lambda execution"
)

print("✅ Role created:", response['Role']['Arn'])

# Step 2: Attach Policy
iam.attach_role_policy(
    RoleName=role_name,
    PolicyArn="arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
)

print("✅ AWSLambdaBasicExecutionRole policy attached")
