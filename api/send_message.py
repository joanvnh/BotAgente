import os
import json
import requests

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def handler(request):
    if not TOKEN or not CHAT_ID:
        return {"statusCode": 400}
    
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, json={"chat_id": CHAT_ID, "text": "Hola!"})
    except:
        pass
    
    return {"statusCode": 200}
