import os
import json
import requests

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def application(environ, start_response):
    path = environ.get("PATH_API", "/")
    method = environ.get("REQUEST_METHOD", "GET")
    
    if path == "/":
        response = "Bot active"
    elif path == "/api/webhook":
        response = "Webhook endpoint"
    elif path == "/api/send_message":
        response = send_message()
    else:
        response = "Not found"
    
    start_response("200 OK", [("Content-Type", "text/plain")])
    return [response.encode()]

def send_message():
    if not TOKEN or not CHAT_ID:
        return "Error: Missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID"
    
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, json={"chat_id": CHAT_ID, "text": "¡Hola! Mensaje automático cada 30 minutos."})
        return "Message sent"
    except Exception as e:
        return f"Error: {str(e)}"