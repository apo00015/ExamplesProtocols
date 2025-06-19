# IoT Sensor ESP8266 + DHT22 + MQTT

Este proyecto utiliza una placa **ESP8266 NodeMCU** y un sensor **DHT22** para medir **temperatura** y **humedad**, y enviar los datos a un **broker MQTT en la nube** (Shiftr.io).

## 📦 Componentes

- ESP8266 NodeMCU (AZ-Delivery)
- Sensor DHT22 (AM2302)
- Resistencia pull-up de 10kΩ (si tu módulo DHT22 no la incluye)
- Protoboard y cables
- Red WiFi (en este caso, hotspot desde un iPhone)

---

## 🔧 Conexiones

| DHT22 Pin | NodeMCU Pin | Descripción       |
|-----------|-------------|-------------------|
| `+`       | 3V3         | Alimentación 3.3V |
| `OUT`     | D4 (GPIO2)  | Pin de datos      |
| `–`       | GND         | Tierra            |

> ⚠️ No usar 5V. La placa ESP8266 funciona a 3.3V.

---

## 🚀 Cómo funciona

1. El ESP8266 se conecta a la red WiFi.
2. Se conecta al broker MQTT (`mqtt-temperature.cloud.shiftr.io`) usando usuario y contraseña.
3. Cada 10 segundos:
   - Lee temperatura y humedad desde el DHT22.
   - Publica los valores en los topics:
     - `casa/salon/temperatura`
     - `casa/salon/humedad`

---

## 📡 Configuración del broker MQTT

- Broker: `mqtt-temperature.cloud.shiftr.io`
- Puerto: `1883`
- Usuario: `mqtt-temperature`
- Contraseña: `mjTW00WWJE41Lsn6`

> Este broker fue creado en [Shiftr.io](https://shiftr.io), una plataforma de visualización y gestión MQTT.

---

## 🧪 MQTT Topics

| Topic                     | Contenido    |
|---------------------------|--------------|
| `casa/salon/temperatura` | Temperatura en ºC |
| `casa/salon/humedad`     | Humedad relativa % |

---

## 🧰 Dependencias (Arduino IDE)

Instala estas librerías desde el Gestor de Librerías:

- **ESP8266WiFi**
- **PubSubClient** (por Nick O'Leary)
- **DHT sensor library** (por Adafruit)
- **Adafruit Unified Sensor** (dependencia del DHT)

---

## 📺 Monitor Serie

- Velocidad: **9600 baudios**
- Ejemplo de salida: