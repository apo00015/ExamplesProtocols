import argparse

from pymodbus.client import ModbusTcpClient

parser = argparse.ArgumentParser(description="Escribir un valor en un Holding Register Modbus.")
parser.add_argument("type", type=str, help="Tipo de operación lectura (r) o escritura (w)")
parser.add_argument("direccion", type=int, nargs="?", help="Dirección del registro (offset)")
parser.add_argument("valor", type=int, nargs="?", help="Valor a escribir en el registro")

args = parser.parse_args()

client = ModbusTcpClient("localhost", port=5020)
client.connect()

if args.type == "r":
    response = client.read_input_registers(address=0, count=10, slave=1)

    if response.isError():
        print("Error:", response)
    else:
        print("Valores leídos de IR:", response.registers)

    response_holding = client.read_holding_registers(address=0, count=10, slave=1)

    if response_holding.isError():
        print("Error:", response_holding)
    else:
        print("Valores leídos de HR:", response_holding.registers)
elif args.type == "w":
    client.write_register(address=args.direccion, value=args.valor, slave=1)

    response_after = client.read_holding_registers(address=0, count=10, slave=1)
    print("Después de escribir:", response_after.registers)
else:
    print("No se reconoce la opción elegida")

client.close()
