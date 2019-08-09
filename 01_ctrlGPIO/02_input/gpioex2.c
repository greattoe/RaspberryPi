#include <stdio.h>
#include <wiringPi.h>

#define SW1  1 // BCM_GPIO 18
#define LED1 4 // BCM_GPIO 23
#define LED2 5 // BCM_GPIO 24

int main (void)
{
  printf("gpio input test~\n");

  wiringPiSetup();

  pinMode(SW1,  INPUT );
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);

  while(1)
  {
    digitalWrite(LED1, 0); // Off
    digitalWrite(LED2, 0); // Off
    
    while(digitalRead(SW1) == 0)
    {
      digitalWrite(LED1, 1); // On
      digitalWrite(LED2, 1); // On
		}
  }
  return 0;
}
