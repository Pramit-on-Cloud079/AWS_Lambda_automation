import boto3

lambda_client = boto3.client('lambda')
iam_client = boto3.client('iam')

# Replace these with your actual Lambda function name and role name
function_name = 'MyAutomatedLambda'
role_name = 'lambda-execution-role'

# Delete Lambda function
try:
    lambda_client.delete_function(FunctionName=function_name)
    print(f"✅ Lambda function '{function_name}' deleted successfully.")
except Exception as e:
    print(f"❌ Error deleting Lambda function: {e}")

# Detach AWSLambdaBasicExecutionRole policy from the role
try:
    iam_client.detach_role_policy(
        RoleName=role_name,
        PolicyArn='arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole'
    )
    print("✅ Detached AWSLambdaBasicExecutionRole policy.")
except Exception as e:
    print(f"⚠️ Could not detach policy (maybe already detached): {e}")

# Delete the IAM role
try:
    iam_client.delete_role(RoleName=role_name)
    print(f"✅ IAM Role '{role_name}' deleted successfully.")
except Exception as e:
    print(f"❌ Error deleting IAM Role: {e}")
