import logging
import random
import time

from opcua import Server

logging.basicConfig(format="%(asctime)s %(levelname)s:%(message)s", level=logging.INFO)

server = Server()
server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

# Crear namespace y objetos
uri = "http://examples.opcua.local"
idx = server.register_namespace(uri)
obj = server.nodes.objects.add_object(idx, "Machine")
temperature = obj.add_variable(idx, "Temperature", 20.0)
motor = obj.add_variable(idx, "MotorRunning", False)
humidity = obj.add_variable(idx, "Humidity", 50.0)
motor.set_writable()

server.start()
logging.info("Servidor OPC UA iniciado...")

try:
    while True:
        temperature.set_value(20.0 + random.random() * 10)
        humidity.set_value(40.0 + random.random() * 20)
        logging.info(f"Humedad: {humidity.get_value()}")
        logging.info(f"Temperature: {temperature.get_value()}")
        logging.info(f"Estado del motor: {motor.get_value()}")
        time.sleep(10)
except Exception:
    server.stop()
    logging.info("Servidor detenido.")
