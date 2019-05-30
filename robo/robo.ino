#include <Servo.h>
Servo FR;
char SerialData;
String str = "";

int FR_pin = 3;


int counter = 0;
void setup() {
  FR.attach(FR_pin);
  
  Serial.begin(9600);
}
void loop() {
  while (!Serial.available()) {} // wait for data to arrive 
  while (Serial.available()){
    if (Serial.available() > 0){
      char SerialData = Serial.read();
      str += SerialData;
      counter++;
      if (counter % 3 == 0){
        Serial.println(str);
        str = "";
      }
    }
  }
//  Serial.println(str);
//  str = "";


  
  
  FR.write(90);
}
