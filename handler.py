import os
import requests

def postToSlack(event, context):
    slack_webhook_url = os.environ["SLACK_WEBHOOK_URL"]
    print(slack_webhook_url)

    data = { "text": "An event occurred"}

    requests.post(slack_webhook_url, json = data)

    print(event)

    return 