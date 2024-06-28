#include <Arduino.h>
#include <BluetoothSerial.h>
#include <WiFi.h>
#include <WiFiUdp.h>
#include <OSCMessage.h>
#include <OSCBundle.h>
#include <OSCData.h>
#include <esp_wifi.h>

char ssid[] = "100A";
char pass[] = "PittsburghPZM";

WiFiUDP Udp;
const unsigned int recive_port = 1342;
const unsigned int LED_PIN = 15;

OSCErrorCode error;
unsigned int ledState = LOW; // LOW means led is *on*

void readMacAddress()
{
  uint8_t baseMac[6];
  esp_err_t ret = esp_wifi_get_mac(WIFI_IF_STA, baseMac);
  if (ret == ESP_OK)
  {
    Serial.printf("%02x:%02x:%02x:%02x:%02x:%02x\n",
                  baseMac[0], baseMac[1], baseMac[2],
                  baseMac[3], baseMac[4], baseMac[5]);
  }
  else
  {
    Serial.println("Failed to read MAC address");
  }
}

void setup()
{
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, ledState); // turn *on* led

  Serial.begin(115200);

  // Connect to WiFi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, pass);
  // WiFi.begin(ssid);

  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");

  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  Serial.println("Starting UDP");
  Udp.begin(recive_port);
  Serial.print("Recieve port: ");
  Serial.println(recive_port);

  Serial.print("[DEFAULT] ESP32 Board MAC Address: ");
  readMacAddress();
}

void led(OSCMessage &msg)
{
  ledState = msg.getInt(0);
  digitalWrite(LED_PIN, ledState);
  Serial.print("/led: ");
  Serial.println(ledState);
}

void loop()
{
  OSCMessage msg;
  int size = Udp.parsePacket();

  if (size > 0)
  {
    while (size--)
    {
      msg.fill(Udp.read());
    }
    if (!msg.hasError())
    {
      msg.dispatch("/led", led);
    }
    else
    {
      error = msg.getError();
      Serial.print("error: ");
      Serial.println(error);
    }
  }
}