import asyncio


async def gpt_4_call():
    print("Iniciando GPT-4")
    await asyncio.sleep(1)
    print("Terminó GPT-4")
    return "Respuesta de GPT-4"


async def claude_3_call():
    print("Iniciando Claude 3")
    await asyncio.sleep(1.5)
    print("Terminó Claude 3")
    return "Respuesta de Claude 3"


async def local_llama_call():
    print("Iniciando Llama local")
    await asyncio.sleep(3)
    print("Terminó Llama local")
    return "Respuesta de Llama local"


async def llamada(numero, semaforo):
    async with semaforo:
        print(f"Iniciando llamada {numero}")
        await asyncio.sleep(1)
        print(f"Terminó llamada {numero}")


async def main():
    print("\nPrueba con los tres modelos:")

    try:
        async with asyncio.timeout(2):
            respuestas = await asyncio.gather(
                gpt_4_call(),
                claude_3_call(),
                local_llama_call()
            )
            print(respuestas)
    except TimeoutError:
        print("Se superó el tiempo de espera de 2 segundos")

    print("\nPrueba de 10 llamadas con máximo 2 al mismo tiempo:")
    semaforo = asyncio.Semaphore(2)
    tareas = []

    for numero in range(1, 11):
        tareas.append(llamada(numero, semaforo))

    try:
        # Acá dejo 10 segundos para ver que terminen las 10 llamadas.
        async with asyncio.timeout(10):
            await asyncio.gather(*tareas)
            print("Terminaron las 10 llamadas")
    except TimeoutError:
        print("Se superó el tiempo de espera")


asyncio.run(main())
