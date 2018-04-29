//Connect RESET pin to GND over a Switch to ring the bell!
//
//
//

#include <ESP8266MQTTClient.h>
#include <ESP8266WiFi.h>
MQTTClient mqtt;

//examples for SERVER string
//  mqtt://test.mosquitto.org:1883"
//  mqtt://user:pass@mosquito.org:1883"
//  mqtt://user:pass@mosquito.org:1883#clientId"

const char SERVER "x.x.x.x" //MQTT Server
const char SSID "SSID" //WLAN SSID
const char WPASS "idontknow" //WLAN PASS
const int PLED 2 //LED Pin

void setup() {
  Serial.begin(115200);
  //Connect WLAN
  WiFi.begin(SSID, WPASS);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  //Send MQTT String
  mqtt.begin(SERVER);
  mqtt.publish("/klingel", "KLINGELING", 0, 0);
  mqtt.handle();

  //LED Feedback
  digitalWrite(PLED,HIGH);
  delay(100);
  digitalWrite(PLED,LOW)
  
  //DeepSleep
  ESP.deepSleep(0);
}

