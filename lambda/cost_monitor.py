import os
import boto3
from datetime import datetime

ce = boto3.client("ce")
sns = boto3.client("sns")

BUDGET = float(os.environ["MONTHLY_BUDGET"])
TOPIC_ARN = os.environ["SNS_TOPIC_ARN"]

def lambda_handler(event, context):

    today = datetime.utcnow().strftime('%Y-%m-%d')
    start = today[:7] + "-01"

    response = ce.get_cost_and_usage(
        TimePeriod={
            'Start': start,
            'End': today
        },
        Granularity='MONTHLY',
        Metrics=['UnblendedCost']
    )

    cost = float(response['ResultsByTime'][0]['Total']['UnblendedCost']['Amount'])

    if cost > BUDGET:
        message = f"AWS monthly cost is ${cost:.2f}, exceeding your budget of ${BUDGET}"

        sns.publish(
            TopicArn=TOPIC_ARN,
            Subject="AWS Cost Alert",
            Message=message
        )

    return {
        "current_cost": cost
    }
