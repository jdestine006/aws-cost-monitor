# AWS Cloud Cost Calculator

## Overview
An automated cloud cost monitoring system that tracks AWS spending and alerts the user when costs exceed a predefined monthly budget. 
The system runs on a scheduled basis and uses the AWS Cost Explorer API to retrieve current spending data. 
If the spending exceeds the configured threshold, the system automatically sends a notification using Amazon SNS.
## Key Services used
    AWS Cost Explorer
    Amazon SNS
    AWS Lambda
    EventBridge
## Key Features 
 ### Automated Cost Monitoring
 Automatically checks AWS spending daily without manual intervention
 ### Budget Alerting  
 If monthly costs exceed the configured threshold, an SNS alert is sent immediately
 ### Serverless Architecture  
 Runs entirely on AWS managed services without requiring infrastructure management
 ### Cost Governance  
 Demonstrates cloud financial management practices used by organizations to monitor and control cloud spending
