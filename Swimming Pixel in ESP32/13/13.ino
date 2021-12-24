#include <Adafruit_NeoPixel.h>   
#include <WiFi.h>
#include <MQTT.h>
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>


//------------------------Defines for Neo-Pixel ring ------------------------------
#define LED_PIN   5  // Which pin on the ESP32 is connected to the NeoPixels? 
#define LED_COUNT 64 // How many NeoPixels are attached to the ESP32?
Adafruit_NeoPixel pixels(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

//---------------------------Defines Wifi and broker Connection ------------------------------
const char ssid[] = "JuergenWalter";
const char pass[] = "44873763559236747268";
const char MQTT_BROKER_ADDRESS[] = "192.168.188.36";

WiFiClient net;
MQTTClient client(50000); //sets maximum message-size to ~25kB

//-------------------------------Defines MQTT topics------------------------------
const char TOPIC_PIXEL[] = "MIDI/SP13";

//-----------------------------Function Prototypes----------------------------------
//Function to establish connection to WiFi and MQTT
void connect();

//-----------------------------Display-Helper-Functions----------------------------------
void log(String message)
{
  Serial.println(message.c_str());
}


void setup() 
{
  Serial.begin(500000);
  
  //------------------------Neo Pixel-------------------------------
  pixels.begin();
  
  //--------------------WIFI & MQTT Connection----------------------------
  
  client.begin(MQTT_BROKER_ADDRESS, net); //Set the IP address directly.
  client.onMessage(messageReceived); //Set wich function to call on receiving a MQTT message
  connect(); //connect to WiFi and MQTT
}

void loop() 
{
  client.loop(); // function to check for new message arrivals

  if (!client.connected()) 
  { 
    connect(); // in case of connection loss, the client reconnects
  }
}

void messageReceived(String &topic, String &input) 
{
  Serial.print("\nMessage received: ");
  Serial.print(input);
  if (topic == TOPIC_PIXEL)
  {
    float Input = input.toFloat();
    float brightness = 255/15*Input;
    for(int i=0; i<LED_COUNT; i++) 
    { 
      pixels.setPixelColor(i, pixels.Color(255, 0, 0));   
      pixels.setBrightness(brightness);
      pixels.show();   // updated pixel colors to the hardware.
    }
  }
}

void connect() 
{
  //--------------------Connection to WiFi---------------
  log("Checking wifi");
 
  WiFi.begin(ssid, pass);
  while (WiFi.status() != WL_CONNECTED) 
  {
    Serial.print("."); 
  }
  
  Serial.print("connected");
  log("\nConnected!");
  delay(2000);
  
  //--------------------Connection to Broker---------------
  log("\nConnecting to Broker");
  String clientId = "user1";
  while (!client.connect(WiFi.macAddress().c_str(), "try", "try")) 
  {
    Serial.print(".");
  }
  
  log("\nConnected!");
  delay(2000);
  
  //---------------Subscribe to Topics--------------------
  client.subscribe(TOPIC_PIXEL);
}
