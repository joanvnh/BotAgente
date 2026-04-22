import os
import json
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /start"""
    await update.message.reply_text("¡Hola! Soy tu bot de Telegram. 👋")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Responde con hola a cualquier mensaje"""
    await update.message.reply_text("¡Hola!")

async def handle_webhook(request):
    """Maneja los webhooks de Telegram"""
    try:
        data = await request.json()
        update = Update.de_json(data, None)
        
        app = Application.builder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
        
        await app.process_update(update)
        return {"ok": True}
    except Exception as e:
        print(f"Error: {e}")
        return {"ok": False, "error": str(e)}

async def handler(request):
    """Manejador principal para Vercel"""
    if request.method == "POST":
        return await handle_webhook(request)
    return {"ok": True, "message": "Bot is running"}
