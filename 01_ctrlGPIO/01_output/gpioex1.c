#include <stdio.h>
#include <wiringPi.h>

#define LED1 4                 // BCM_GPIO 23
#define LED2 5                 // BCM_GPIO 24

int main (void)
{
  printf("Control GPIO by wiringPi\n");

  wiringPiSetup();

  pinMode (LED1, OUTPUT);
  pinMode (LED2, OUTPUT);

  while(1)
  {
    digitalWrite (LED1, HIGH); // On
    digitalWrite (LED2, HIGH); // On

    delay (500) ;              // (ms)

    digitalWrite (LED1, LOW ); // Off
    digitalWrite (LED2, LOW ); // Off

    delay (500) ;              // (ms)
  }
  return 0;
}
