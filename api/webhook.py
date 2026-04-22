import os
import json
import requests

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_message(chat_id, text):
    """Envía un mensaje a través de la API de Telegram"""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    try:
        response = requests.post(url, json=payload)
        return response.status_code == 200
    except:
        return False

def handler(request):
    """Manejador del webhook de Telegram para Vercel"""
    try:
        if request.method == "GET":
            return {
                "statusCode": 200,
                "body": json.dumps({"ok": True, "message": "Bot running"})
            }
        
        if request.method == "POST":
            # Parse JSON from body
            body = request.get_json()
            
            if not body or "message" not in body:
                return {
                    "statusCode": 200,
                    "body": json.dumps({"ok": True})
                }
            
            msg = body["message"]
            if "text" in msg:
                chat_id = msg["chat"]["id"]
                send_message(chat_id, "Hola")
            
            return {
                "statusCode": 200,
                "body": json.dumps({"ok": True})
            }
        
        return {
            "statusCode": 200,
            "body": json.dumps({"ok": True})
        }
    except Exception as e:
        return {
            "statusCode": 200,
            "body": json.dumps({"ok": True})
        }
