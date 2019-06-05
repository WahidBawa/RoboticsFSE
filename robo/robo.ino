#include <Servo.h>
Servo FR;
char SerialData;
String str = "";

int FR_pin = 3;


int counter = 0;
int len = 0;

bool readyToGetVal = false;
bool readyToGetLength = true;
void setup() {
  FR.attach(FR_pin);

  Serial.begin(9600);
}
void loop() {
  if (readyToGetLength){
    while (!Serial.available()) {} // wait for data to arrive 
    while (Serial.available()){
      if (Serial.available() > 0){
        char SerialData = Serial.read();
        str += SerialData;
        counter++;
        if (counter == 2){
          len = str.toInt();
          Serial.println(len);
          str = "";
          counter = 0;
          readyToGetVal = true;
          readyToGetLength = false;
        }
      }
    } 
  }

  
  while (!Serial.available()) {} // wait for data to arrive 
  while (Serial.available()){
    if (Serial.available() > 0){
      char SerialData = Serial.read();
      str += SerialData;
      counter++;
      if (counter == 16){
        Serial.println(str.toInt());
        str = "";
        counter = 0;
        readyToGetVal = true;
        readyToGetLength = false;
      }
    }
  }
//  Serial.println(str);
//  str = "";


  
  
  FR.write(180);
}
