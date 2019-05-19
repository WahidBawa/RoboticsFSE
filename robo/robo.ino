#include <Servo.h>
Servo servo;
int x = A0;
int xVal;
void setup() {
  pinMode(x, INPUT);
  servo.attach(3);
  servo.write(90);
  Serial.begin(9600);
}
void loop() {
  xVal = map(analogRead(x), 0, 1024, 40, 140);
  Serial.println(xVal);
  servo.write(xVal);
}
