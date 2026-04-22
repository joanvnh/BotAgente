import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_periodic_message():
    """Envía 'Hola' cada 30 minutos"""
    if not TOKEN or not CHAT_ID:
        return {"error": "TOKEN o CHAT_ID no configurados", "ok": False}
    
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

def handler(request):
    """Manejador para Vercel"""
    result = send_periodic_message()
    return result
