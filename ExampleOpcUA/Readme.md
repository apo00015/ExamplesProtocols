
# 🌐 Servidor OPC UA Simulado en Python

Este proyecto implementa un **servidor OPC UA básico en Python** utilizando la librería `opcua`, el cual simula sensores de una máquina industrial como **temperatura**, **humedad** y el estado de un **motor**.

## Ejecución del servidor OPC

Para poder ejecutar el servidor, bastará con levantar los contenedores con los siguientes comandos

```bash
docker build -t opcua-server-image .
docker run --name opcua_server -p 4840:4840 opcua-server-image
```

## Funcionamiento del servidor OPC

- Expone un endpoint accesible en: opc.tcp://0.0.0.0:4840/freeopcua/server/
- Publica tres variables bajo un nodo llamado Machine:
  - Temperature: valor tipo Float, entre 20 y 30 °C.
  - Humidity: valor tipo Float, entre 40 y 60 %.
  - MotorRunning: valor Boolean que puede ser escrito desde un cliente.
- Actualiza los valores de temperatura y humedad cada 10 segundos.

# 🔌 Cliente OPC UA en Python

Este proyecto implementa un **cliente OPC UA básico** en Python que se conecta a un servidor OPC UA, **lee el valor de un nodo** específico y, si se indica, **escribe un nuevo valor booleano** en dicho nodo.

## 📦 Requisitos

- Python 3.7 o superior
- Librería [`opcua`](https://pypi.org/project/opcua/)

### 📥 Instalación

```bash
pip install opcua
```

## Ejecución del cliente OPC

```bash
python3 cliente_opc.py <child> <valor>
```

### Parámetros

| Parámetro  |  Tipo | Descripción  | Obligatorio |
|---|---|---|---|
| type  | string  |  Nombre del nodo hijo dentro de Machine | Sí |
|  valor | bool  | Valor booleano a escribir (true, false) en el motor | No, solo si se desea modificar el valor del motor |

## Funcionamiento del cliente OPC

- Conectarse a un servidor OPC UA en opc.tcp://localhost:4840/freeopcua/server/
- Navegar al nodo "Machine" dentro de Objects
- Leer el valor de una variable indicada
- Escribir un nuevo valor booleano si se proporciona como argumento
