#include <Servo.h>

Servo pan, tilt;

String inputString = "";
boolean stringComplete = false;

int posPan  = 90;
int posTilt = 65;

void setup() {
  pan.attach(9);
  tilt.attach(10);
  pan.write(posPan );   delay(15);
  tilt.write(posTilt);  delay(15);
  Serial.begin(9600);
  inputString.reserve(10);
}
/*
 pan1     til5
 pan90    til60
 pan180   til120
 */
void loop() {
  if (stringComplete == true) {
    if(inputString.substring(0,3) == "pan") {
      posPan = (inputString.substring(3)).toInt();
    }
    else if(inputString.substring(0,4) == "tilt"){
      posTilt = (inputString.substring(4)).toInt();
    }
    else;

    pan.write(posPan );   delay(15);
    tilt.write(posTilt);  delay(15);
    inputString = "";
    stringComplete = false;
  }
}

/* serial recieve interrupt service routine */
void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    inputString = inputString + inChar;
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}
