#include <Servo.h>
Servo servo;
void setup() {
  servo.attach(3);
}
void loop() {
  servo.write(90);       
}
