from modules.handlers.mp3_handler import handle_mp3
from modules.handlers.mp4_handler import handle_mp4
from core.queue_system import agregar_tarea

async def manejar_comando(update, context):
    texto = update.message.text.split()

    if len(texto) < 2:
        await update.message.reply_text("❌ Uso:\n/mp3 link\n/mp4 link [5 o 10]")
        return

    comando = texto[0]

    await update.message.reply_text("📥 Añadido a la cola...")

    async def tarea():
        if comando == "/mp3":
            await handle_mp3(update, context, texto)

        elif comando == "/mp4":
            await handle_mp4(update, context, texto)

        else:
            await update.message.reply_text("❌ Comando no válido")

    await agregar_tarea(tarea)