#include <Servo.h>
Servo servo;
int x = A0;
int xVal;
int owo;
void setup() {
  pinMode(x, INPUT);
  servo.attach(3);
  servo.write(90);
  Serial.begin(9600);
}
void loop() {
  xVal = analogRead(x);
//  Serial.println(xVal);
  owo = map(xVal, 0, 1024, 40, 140);
  Serial.println(owo);
  servo.write(owo);
}
