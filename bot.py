import asyncio
from telegram.ext import ApplicationBuilder, MessageHandler, filters

from config import TOKEN
from core.worker import worker
from modules.handlers.command_handler import manejar_comando

async def comandos(update, context):
    await manejar_comando(update, context)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, comandos))
    app.add_handler(MessageHandler(filters.COMMAND, comandos))

    loop = asyncio.get_event_loop()

    # 🔥 workers paralelos
    for _ in range(2):
        loop.create_task(worker())

    print("👑 KHASAM BOT IMPERIO ACTIVO")
    app.run_polling()

if __name__ == "__main__":
    main()