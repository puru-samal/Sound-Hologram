#include <Arduino.h>
#include <BluetoothSerial.h>
#include <WiFi.h>
#include <WiFiUdp.h>
#include <OSCMessage.h>
#include <OSCBundle.h>
#include <OSCData.h>
#include <esp_wifi.h>

// char ssid[] = "CMU-DEVICE";
// char pass[] = "PittsburghPZM";
char ssid[] = "sound-hologram";
char pass[] = "spatial_";

WiFiUDP Udp;
const unsigned int recive_port = 1342;
const unsigned int LED_PIN = 15;

// Define Static IP addr, gatewat and subnet_mask
// Usable range : 172.16.1.[1..254]
IPAddress local_IP(172, 16, 1, 1);
IPAddress gateway(172, 16, 1, 1);
IPAddress subnet(255, 255, 255, 0);

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

  // Set ESP32 as an access point
  Serial.println("Configuring access point...");
  WiFi.softAPConfig(local_IP, gateway, subnet);
  if (!WiFi.softAP(ssid, pass))
  {
    log_e("Soft AP creation failed.");
    while (1)
      ;
  }

  // Print IP addr
  IPAddress myIP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(myIP);

  // Start UDP
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