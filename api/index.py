import json

def handler(request):
    """Endpoint raíz - verifica que el bot está activo"""
    return {
        "statusCode": 200,
        "body": json.dumps({"ok": True, "message": "Bot de Telegram está activo"})
    }
