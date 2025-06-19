# Esclavo Modbus TCP en Python

Este proyecto implementa un servidor Modbus TCP simulado usando la librería pymodbus. El servidor actúa como un dispositivo esclavo industrial, actualizando periódicamente sus registros de entrada con valores aleatorios, lo que permite simular datos de sensores reales para pruebas o desarrollos sin hardware físico.

## Ejecución del esclavo Modbus

Para poder ejecutar el servidor, bastará con levantar los contenedores con los siguientes comandos

```bash
docker build -t modbus-server .
docker run --name modbus_slave -p 5020:5020 modbus-server
```

## Funcionamiento del esclavo Modbus

- Inicia un servidor Modbus TCP asíncrono.
- Define 4 bloques de memoria:
  - HR (Holding Registers): lectura/escritura
  - IR (Input Registers): solo lectura
  - CO (Coils): lectura/escritura de bits
  - DI (Discrete Inputs): solo lectura de bits
- Cada 5 segundos, actualiza automáticamente los Input Registers (IR) con valores aleatorios entre 1 y 10 para simular mediciones dinámicas (como temperatura, presión, etc)

# Maestro Modbus TCP en Python

Este script permite simular un cliente Modbus TCP capaz de realizar lecturas y escrituras en un servidor/esclavo Modbus utilizando la librería pymodbus.

## Requisitos

- Python 3.8+
- Librería pymodbus

### Instalación

```bash
pip install pymodbus
```

## Ejecución del maestro Modbus

```bash
python3 master_modbus.py <tipo_operacion> [direccion] [valor]
```

### Parámetros

| Parámetro  |  Tipo | Descripción  | Obligatorio |
|---|---|---|---|
| type  | string  |  Tipo de operación: "r" para lectura, "w" para escritura | En ambos casos |
| direccion  | int  | Dirección del registro a leer o escribir (offset) | Solo en w |
|  valor | bool  |  Valor a escribir en el registro | Solo en w |

## Funcionamiento del maestro Modbus

El script asume que hay un servidor Modbus TCP escuchando en:

- Host: localhost
- Puerto: 5020
- Slave ID: 1
