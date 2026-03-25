from modules.handlers.loader import cargar_handlers, get_handler
from core.queue_system import agregar_tarea
from database.db import registrar_usuario

cargar_handlers()

async def manejar_comando(update, context):
    texto = update.message.text.split()
    user = update.message.from_user

    registrar_usuario(user.id, user.username)

    if len(texto) < 2:
        await update.message.reply_text("❌ Uso:\n/mp3 link\n/mp4 link [5 o 10]")
        return

    comando = texto[0]
    handler = get_handler(comando)

    if not handler:
        await update.message.reply_text("❌ Comando no existe")
        return

    await update.message.reply_text("📥 Añadido a la cola...")

    async def tarea():
        await handler(update, context, texto)

    await agregar_tarea(tarea)