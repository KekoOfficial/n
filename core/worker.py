import asyncio
from core.queue_system import obtener_tarea

async def worker():
    while True:
        tarea = await obtener_tarea()

        try:
            await tarea()
        except Exception as e:
            print(f"Error en tarea: {e}")

        await asyncio.sleep(1)