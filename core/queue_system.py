import asyncio

cola = asyncio.Queue()

async def agregar_tarea(tarea):
    await cola.put(tarea)

async def obtener_tarea():
    return await cola.get()