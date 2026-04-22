import os
import json
import requests

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def send_msg(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

def main(request):
    if request.method == "GET":
        return {"statusCode": 200, "body": "Bot is running"}
    
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            if "message" in data and "text" in data["message"]:
                chat_id = data["message"]["chat"]["id"]
                send_msg(chat_id, "Hola")
        except:
            pass
    
    return {"statusCode": 200}
