import json
import urllib3

def lambda_handler(event, context):
    try:
        # Log the incoming event for debugging
        print("Received event:", json.dumps(event))
        
        # Extract SNS message
        sns_record = event['Records'][0]['Sns']
        raw_message = sns_record['Message']
        
        print(f"Raw message type: {type(raw_message)}")
        print(f"Raw message: {raw_message}")
        
        # Handle both string and dict
        if isinstance(raw_message, str):
            message = json.loads(raw_message)
        else:
            message = raw_message
        
        print("Parsed message:", json.dumps(message))
        
        # Webhook URL
        webhook_url = 'WEBHOOK_URL_PLACEHOLDER'
        
        # Determine color based on status
        status = message.get('status', '').lower()
        color = "good" if "success" in status else "danger"
        
        # Format message for Slack
        slack_message = {
            "text": "🚀 Deployment Notification",
            "attachments": [{
                "color": color,
                "fields": [
                    {"title": "Status", "value": message.get('status', 'Unknown'), "short": True},
                    {"title": "Environment", "value": message.get('environment', 'N/A'), "short": True},
                    {"title": "Build Number", "value": str(message.get('build', 'N/A')), "short": True},
                    {"title": "App", "value": message.get('app', 'N/A'), "short": True},
                    {"title": "Component", "value": message.get('component', 'N/A'), "short": True},
                    {"title": "Timestamp", "value": message.get('timestamp', ''), "short": False}
                ]
            }]
        }
        
        print("Sending to Slack:", json.dumps(slack_message))
        
        # Send to Slack
        http = urllib3.PoolManager()
        response = http.request('POST', webhook_url, 
                               body=json.dumps(slack_message),
                               headers={'Content-Type': 'application/json'})
        
        print(f"Slack response status: {response.status}")
        print(f"Slack response: {response.data.decode('utf-8')}")
        
        return {
            'statusCode': 200,
            'body': json.dumps('Successfully sent to Slack')
        }
        
    except Exception as e:
        print(f"ERROR: {str(e)}")
        import traceback
        print(f"Traceback: {traceback.format_exc()}")
        print(f"Full event: {json.dumps(event)}")
        raise e