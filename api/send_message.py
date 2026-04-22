import os
import json
import requests

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def handler(request):
    """Manejador para enviar mensajes automáticos"""
    try:
        if not TOKEN or not CHAT_ID:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Config missing"})
            }
        
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": "Hola! Mensaje cada 30 minutos"
        }
        
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            return {
                "statusCode": 200,
                "body": json.dumps({"ok": True, "message": "Message sent"})
            }
        else:
            return {
                "statusCode": 500,
                "body": json.dumps({"ok": False, "error": response.text})
            }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"ok": False, "error": str(e)})
        }
