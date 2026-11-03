# Orquestador concurrente de modelos

Ejercicio de Python asíncrono de Coderhouse.

Simulo tres llamadas a modelos con distintos tiempos de respuesta. Se ejecutan con `asyncio.gather()` y un límite total de dos segundos usando `asyncio.timeout(2)`. Si se supera ese tiempo, se captura `TimeoutError`.

Después simulo diez llamadas y uso `asyncio.Semaphore(2)` para permitir como máximo dos ejecuciones al mismo tiempo. En esta segunda prueba dejo diez segundos de timeout para observar que terminen todas.

## Ejecutar

Necesitás Python 3.12 o superior. No hay que instalar dependencias.

```bash
python orquestador.py
```

No se conectan APIs reales: las llamadas se simulan con `asyncio.sleep()`.
