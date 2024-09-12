import base64  
import requests  
import urllib.parse  
import os

def lambda_handler(event, context):  

    # Check if the body is Base64 encoded  
    if event.get('isBase64Encoded', False):  
        # Decode the Base64 body  
        body = base64.b64decode(event['body']).decode('utf-8')  
    else:  
        # If it's not Base64 encoded, just take the body out of the JSON  
        body = event['body']  

    # Converts into a dictionary
    twilio_data = urllib.parse.parse_qs(body)  

    # Unwrap the list values  
    twilio_data = {key: value[0] for key, value in twilio_data.items()} 
    
    discord_webhooks = {
        os.environ['dev_it_number']: os.environ['dev_it_webhook'],
        os.environ['marketing_number']: os.environ['marketing_webhook'],
        os.environ['breaking_number']: os.environ['breaking_webhook'],
        os.environ['hr_number']: os.environ['hr_webhook']
    }
    # Formats the message for Discord output
    if 'Body' in twilio_data and 'From' in twilio_data:  
        message_content = f"{twilio_data['From']}\n{twilio_data['Body']}"  
    else:  
        message_content = "Received text message in invalid format. Check Twilio logs for more info."  

    message_payload = {  
        "content": message_content  
    }  

    # Sends Discord POST request
    if str(twilio_data["To"]) in discord_webhooks:
        response = requests.post(discord_webhooks[str(twilio_data["To"])], json=message_payload)

    if response.status_code != 204:  
        return {  
            'statusCode': 500,  
        }  

    return {  
        'statusCode': 200,  
    }