#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <wiringPi.h>

#define TRIG 24	
#define ECHO 25

int trig(void)
{
	digitalWrite( TRIG, HIGH );
	delayMicroseconds( 10 );
	digitalWrite( TRIG, LOW  );
}

unsigned long echo(void)
{
	unsigned long time = 0;
	
	while( digitalRead( ECHO ) == LOW  );
	time = micros();
	while( digitalRead( ECHO ) == HIGH );
	time = micros() - time;
	
	if( time >= 240 && time <= 23000 )	return time;
	
	else	return 0;
}

int main (void)
{
	int data;

	unsigned long echo_time = 0;
	unsigned long dist = 0;
  
	wiringPiSetup();
	
	pinMode( ECHO, INPUT  );
	pinMode( TRIG, OUTPUT );
	digitalWrite( TRIG, LOW );
  
	printf ("\nHC-SR04 Test~\n");
  
	while(1)
	{
		trig();
		echo_time = echo();
		
		if( echo_time != 0 )
		{
			// 340000mm / 1000000us = 2 * dist / echo_time
			// 340000 * echo_time = 2 * dist * 1000000
			// dist = 340000 * echo_time / 2000000
			// dist = 17 * echo_time / 100
			dist = 17 * echo_time / 100;
			printf("distance = %4d (mm)\n",dist);
		}
		else
			printf("out of range!!!\n",dist);
		
		delay(1000);
	}
	return 0;
}
