import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def handler(request):
    """Manejador para enviar mensajes automáticos (llamado por crons)"""
    
    if not TOKEN or not CHAT_ID:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": "TOKEN o CHAT_ID no configurados",
                "ok": False
            })
        }
    
    result = send_periodic_message()
    return {
        "statusCode": 200 if result["ok"] else 500,
        "body": json.dumps(result)
    }

def send_periodic_message():
    """Envía 'Hola' cada 30 minutos"""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": "¡Hola! 👋 Mensaje automático cada 30 minutos"
    }
    
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return {"ok": True, "message": "Mensaje enviado"}
        else:
            return {"ok": False, "error": response.text}
    except Exception as e:
        return {"ok": False, "error": str(e)}
