import argparse

from opcua import Client


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ("yes", "true", "t", "1"):
        return True
    elif v.lower() in ("no", "false", "f", "0"):
        return False
    else:
        raise argparse.ArgumentTypeError("Valor booleano esperado (true/false)")


parser = argparse.ArgumentParser(description="Nodos en el protocolo OPC UA")
parser.add_argument("child", type=str, help="Nodo al que acceder")
parser.add_argument("valor", type=str2bool, nargs="?", help="Valor a escribir en el nodo")

args = parser.parse_args()

client = Client("opc.tcp://localhost:4840/freeopcua/server/")
client.connect()
print("Cliente conectado al servidor.")

try:
    # Buscar los nodos
    root = client.get_root_node()
    machine = root.get_child(["0:Objects", "2:Machine"])
    node_object = machine.get_child(f"2:{args.child}")

    print(f"{args.child}:", node_object.get_value())

    if args.valor is not None:
        node_object.set_value(args.valor)
except Exception:
    print(f"No se ha podido conectar con el nodo: {args.child}")


client.disconnect()
