#include <Servo.h>
int FL_pin = 6;
Servo FL;

int BL_pin = 5;
Servo BL;

int FR_pin = 4;
Servo FR;

int BR_pin = 3;
Servo BR;

void setup() {
  FL.attach(FL_pin);
  BL.attach(BL_pin);
  FR.attach(FR_pin);
  BR.attach(BR_pin);

  Serial.begin(9600);
}

void loop() {
  FL.write(80); // 90< for forward, 90> for backwards
  BL.write(80); // 90< for forward, 90> for backwards
  
  FR.write(100); // 90> for forward, 90< for backwards
  BR.write(100); // 90> for forward, 90< for backwards
}
