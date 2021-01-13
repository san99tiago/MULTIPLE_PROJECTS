// MAIN HARDWARE CHALLENGE FOR MLH 2021 LOCAL HACK DAY
// Create an IOT-based counter system hosted on php-based servers...
// ...including all WordPress approaches.
//---------------------------------------------------------------------------

#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266HTTPClient.h>

// TESTS (MUST FILL INFO):
const char* ssid     = "";
const char* password = "";
String host = "";
String port = ":80";
String extra_path = "send_data_to_mysql.php";
String payload = "";


// Identify the machine's ID
String DEVICE_ID = "555";

// Main variables for the sensors and logic
int counter = 0;
int time_ms = 0;
bool current_state = LOW;
bool previous_state = LOW;


void setup() {
  // Main pin for the sensor connected to the ESP8266 
  pinMode(2, INPUT_PULLUP);

  // Apply a serial-communication baudrate of 9600
  Serial.begin(9600);

  delay(2000);

  // Connect to main wifi (change variables at the beggining)
  Serial.println("Initialize connection...");
  WiFi.begin(ssid, password);

  Serial.println("CONNECTING...");

  // Wait for proper connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
}


void loop() {


  if (digitalRead(2) == LOW){
    current_state = HIGH;
  }else{
    current_state = LOW;
  }

  if (current_state == HIGH && previous_state == LOW){
      counter = counter + 1;
  }
  previous_state = current_state;


  String str_current_state = String(current_state);
  String str_previous_state = String(previous_state);
  String str_counter = String(counter);

  WiFiClient client;


  // Send post to server each X amout of seconds (60 is aprox 1 min)
  if (time_ms > 60) {
    if (WiFi.status() == WL_CONNECTED) {

      String postData = "test=" + DEVICE_ID + "&counter=" + str_counter + ";";
      MAKE_POST(postData);
      
      time_ms = 0;
      counter = 0;

    }else{
      Serial.println("NO_WIFI");
      // If we loose connection, try to get it back
      WiFi.begin(ssid, password);

      Serial.println("CONNECTING...");
      
      // Wait for correct connection resolved
      while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
      }
    }
  }

  time_ms = time_ms + 1;
  delay(999);

}




// MAIN POST FUNCTION
void MAKE_POST(String value) {
  // It is the real path to get the url web server
  HTTPClient http; //Declare an object of class HTTPClient
  String url = host + port + "/" + extra_path;

  Serial.println("STARTING_POST....");
  // Specify request destination (start connection HTTP from ESP to SERVER)
  if (http.begin( url )  )
  {
    // It is important to explicitly say which format is going to be send
    http.addHeader("Content-Type" , "application/x-www-form-urlencoded");

    // Create main POST for the server
    int httpCode = http.POST( value );


    // Check for recieving a real HTTP code
    if (httpCode > 0) {

      // It means that the recieved code is 200 (everything is fine)
      if ( httpCode == HTTP_CODE_OK || HTTP_CODE_MOVED_PERMANENTLY){
        
        // Show recieved info directly by serial
        Serial.print("SERVER_POST_OK:");
        Serial.println( http.getString() );

      
      }else{
        // Try to check if there is a problem with the recieved httpcode
        Serial.print("SERVER_POST_BAD_HTTP_CODE:");
        Serial.println( httpCode );
      }

    }else{
      Serial.println("SERVER_NOT_CONNECTED");     
    }

    // Always end http connection for better performance
    http.end();

  }else{
    // If main conneciton didn't work
    Serial.println("SERVER_NOT_CONNECTED");
  }

}
