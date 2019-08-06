#include <stdio.h>
#include <wiringPi.h>

#define MAXTIMINGS    85
#define DHTPIN         7

int dht11_dat[5] = { 0, 0, 0, 0, 0 };
 
void read_dht11_dat()
{
  unsigned char laststate	= HIGH;
  unsigned char counter	= 0;
  unsigned char j	= 0, i;
  float f; 

  dht11_dat[0] = dht11_dat[1] = dht11_dat[2] = dht11_dat[3] = dht11_dat[4] = 0;

  pinMode(DHTPIN, OUTPUT);
  digitalWrite(DHTPIN, LOW);
  delay(18);

  digitalWrite(DHTPIN, HIGH);
  delayMicroseconds(40);

  pinMode(DHTPIN, INPUT);

  for(i = 0; i < MAXTIMINGS; i++)
  {
    counter = 0;
    while(digitalRead(DHTPIN) == laststate)
    {
      counter++;
      delayMicroseconds(1);
      if(counter == 255)  break;
    }
    laststate = digitalRead(DHTPIN);

    if(counter == 255)  break;

    if((i >= 4) && (i % 2 == 0))
    {
      dht11_dat[j / 8] <<= 1;
      if(counter > 50 /*16*/)
        dht11_dat[j / 8] |= 1;
      j++;
    }
  }

  if((j >= 40) && (dht11_dat[4] == ((dht11_dat[0] + dht11_dat[1] + dht11_dat[2] + dht11_dat[3]) & 0xFF)))
  {
    // f = dht11_dat[2] * 9. / 5. + 32;
    printf(" T = %d.%d *C, H = %d.%d %%\n", dht11_dat[2], dht11_dat[3], dht11_dat[0], dht11_dat[1]);
  }
  else  printf("data read error, skip\n");
}
 
void main()
{
  wiringPiSetup();
  
  printf("Get Temperature & Humidity from DHT11~\n" );

  while(1)
  {
    read_dht11_dat();
    delay(2000); 
  }
}