# AWS Lambda Automation using Python (Boto3)

## 🚀 Project Overview

This project automates the creation of an AWS Lambda function using Python and the Boto3 SDK.  
It includes:

- Programmatic creation of an IAM role with the correct trust policy for Lambda
- Attachment of `AWSLambdaBasicExecutionRole` policy
- Automated deployment of a Lambda function using a ZIP file
- Future-ready for enhancements like environment variables, event triggers, or dynamic code uploads

---

## 🛠 Tech Stack

- AWS IAM
- AWS Lambda
- Python 3.11
- Boto3 SDK

---

## 📁 Project Structure

aws-lambda-automation/
│
├── create_lambda_role.py # Creates IAM role for Lambda
├── deploy_lambda_function.py # Deploys Lambda function using ZIP
├── lambda_function/
│ └── lambda_function.py # Sample Lambda code (returns Hello from Lambda!)
│
├── lambda_function.zip # Zipped package for deployment
└── README.md


---

## ✅ Outcome

- Created Lambda IAM Role with trust policy
- Attached required execution policy
- Uploaded and deployed the function using automation
- Screenshot proof included

---

## 📸 Screenshots

(Screenshots added here in the GitHub repo)

---

## 🤖 Future Enhancements

- Add EventBridge trigger automation
- Enable CloudWatch logging and monitoring setup
- Include CI/CD integration (CodePipeline)

---

## 🎯 Why this project matters

AWS Lambda is central to serverless architecture. Automating its deployment using code prepares you for:

- Real-world DevOps roles  
- CI/CD pipelines  
- Scalable cloud-native application development

---

## 🔗 Author

**Pramit Dasgupta**  
AWS Cloud Solutions Architect (in training)  