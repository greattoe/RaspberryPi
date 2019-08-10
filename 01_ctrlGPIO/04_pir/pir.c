#include <stdio.h>
#include <wiringPi.h>

#define PIR 1
#define LED1 4
#define LED2 5

int main(void)
{
  printf("PIR Sensor Test\n");
  
  wiringPiSetup( );
  
  pinMode(PIR,  INPUT );
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  
  while(1)
  {
    if( digitalRead(PIR) == 0 )
    {
      digitalWrite(4, 0);
      digitalWrite(5, 1);
    }
    else
    {
      digitalWrite(4, 1);
      digitalWrite(5, 0);
    }
  }
  return 0;
}