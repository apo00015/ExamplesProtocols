import asyncio
import logging
import random

from pymodbus.datastore import ModbusSequentialDataBlock, ModbusServerContext, ModbusSlaveContext
from pymodbus.server import StartAsyncTcpServer

logging.basicConfig(format="%(asctime)s %(levelname)s:%(message)s", level=logging.INFO)

store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0] * 10),
    co=ModbusSequentialDataBlock(0, [0] * 10),
    hr=ModbusSequentialDataBlock(0, [1] * 10),
    ir=ModbusSequentialDataBlock(0, [0] * 10),
)


context = ModbusServerContext(slaves={1: store}, single=False)

logging.info(f"Holding Registers (HR): {store.getValues(3, 0, count=10)}")
logging.info(f"Input Registers (IR): {store.getValues(4, 0, count=10)}")
logging.info(f"Coils (CO): {store.getValues(1, 0, count=10)}")
logging.info(f"Discrete Inputs (DI): {store.getValues(2, 0, count=10)}")


async def actualizar_valores():
    while True:
        nuevos_valores = [random.randint(1, 10) for _ in range(10)]
        store.setValues(4, 0, nuevos_valores)
        logging.info(f"IR actualizados: {nuevos_valores}")
        await asyncio.sleep(5)


async def run_server():
    await asyncio.gather(StartAsyncTcpServer(context, address=("0.0.0.0", 5020)), actualizar_valores())


try:
    asyncio.run(run_server())
except RuntimeError as e:
    if "asyncio.run() cannot be called from a running event loop" in str(e):
        loop = asyncio.get_event_loop()
        loop.create_task(run_server())
        loop.run_forever()
    else:
        raise
