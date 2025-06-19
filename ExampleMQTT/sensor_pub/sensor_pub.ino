#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>

// CONFIGURACIÓN
#define DHTPIN 2   // D4 = GPIO2 en NodeMCU
#define DHTTYPE DHT22

const char* ssid = "iPhone adri";
const char* password = "adri98766";

const char* mqtt_user = "mqtt-temperature";
const char* mqtt_pass = "mjTW00WWJE41Lsn6";
const char* mqtt_server = "mqtt-temperature.cloud.shiftr.io";
const int mqtt_port = 1883;

DHT dht(DHTPIN, DHTTYPE);
WiFiClient espClient;
PubSubClient client(espClient);

// Conectar WiFi
void setup_wifi() {
  delay(10);
  Serial.println("Conectando a WiFi...");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("\nConectado a red WiFi");
  Serial.println(WiFi.localIP());
}

// Reconectar MQTT si se pierde
void reconnect() {
  while (!client.connected()) {
    Serial.print("Intentando conexión MQTT...");
    if (client.connect("ESP8266Client", mqtt_user, mqtt_pass)) {
      Serial.println("conectado");
    } else {
      Serial.print("falló (rc=");
      Serial.print(client.state());
      Serial.println("), reintentando...");
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(9600);
  dht.begin();
  setup_wifi();
  client.setServer(mqtt_server, 1883);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

 // Leer temperatura y humedad
  float temp = dht.readTemperature();
  float hum = dht.readHumidity();

  if (isnan(temp) || isnan(hum)) {
    Serial.println("Error al leer el sensor DHT");
    return;
  }

  // Publicar temperatura
  char payloadTemp[8];
  dtostrf(temp, 4, 2, payloadTemp);
  client.publish("casa/salon/temperatura", payloadTemp);
  Serial.print("Temperatura publicada: ");
  Serial.println(payloadTemp);

  // Publicar humedad
  char payloadHum[8];
  dtostrf(hum, 4, 2, payloadHum);
  client.publish("casa/salon/humedad", payloadHum);
  Serial.print("Humedad publicada: ");
  Serial.println(payloadHum);

  delay(10000);
}

