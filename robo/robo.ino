#include <Servo.h>
Servo servo;
int xVal;
char SerialData;
String str = "";
void setup() {
  servo.attach(3);
  servo.write(90);
  Serial.begin(9600);
}
void loop() {
//  xVal = map(analogRead(x), 0, 1024, 40, 140);
//  Serial.println(xVal);
  while (!Serial.available()) {} // wait for data to arrive
  while (Serial.available()){
    char SerialData = Serial.read();
    str += SerialData;
  }
  Serial.println(str);
//  str = "";
  servo.write(90);
}
