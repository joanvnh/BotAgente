import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def handler(request):
    """Manejador del webhook de Telegram para Vercel"""
    
    # GET request - verifica que el bot está funcionando
    if request.method == "GET":
        return {
            "statusCode": 200,
            "body": json.dumps({"ok": True, "message": "Bot is running"})
        }
    
    # POST request - procesa mensajes de Telegram
    if request.method == "POST":
        try:
            # Parsear el JSON del request
            if isinstance(request.body, bytes):
                data = json.loads(request.body.decode())
            else:
                data = json.loads(request.body)
            
            # Verifica que sea un mensaje
            if "message" not in data:
                return {
                    "statusCode": 200,
                    "body": json.dumps({"ok": True})
                }
            
            message = data["message"]
            chat_id = message["chat"]["id"]
            text = message.get("text", "")
            
            # Responde "¡Hola!" a cualquier mensaje
            if text:
                send_message(chat_id, "¡Hola! 👋")
            
            return {
                "statusCode": 200,
                "body": json.dumps({"ok": True})
            }
            
        except Exception as e:
            print(f"Error: {e}")
            return {
                "statusCode": 200,
                "body": json.dumps({"ok": True})
            }
    
    return {
        "statusCode": 405,
        "body": json.dumps({"error": "Method not allowed"})
    }

def send_message(chat_id, text):
    """Envía un mensaje a través de la API de Telegram"""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text
    }
    try:
        response = requests.post(url, json=data)
        return response.status_code == 200
    except Exception as e:
        print(f"Error al enviar mensaje: {e}")
        return False
