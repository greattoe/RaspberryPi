#include <stdio.h>
#include <wiringPi.h>
#include <softPwm.h> 

#define SERVO  21	// BCM 5
#define MAX    23
#define MIN     7

int ch2no(unsigned char ch);

int main()
{
  unsigned char ch;
	unsigned int  offset =  1;
	unsigned int  pos    = 15;
  
	unsigned int preset[5]  = { 7, 11, 15, 19, 23 }; 

  if(wiringPiSetup() == -1)  return 1;

  softPwmCreate(SERVO,  0, 200);
  
  printf("select preset position(1 ~ 5) ");
  printf("or '>' for cw, '<' for ccw move.\n>");
  
	while(ch != 'Q')
  {
    printf(">"); ch = getchar();
    
    if( ch != '\n' && ch != '\r' )
    {
      if     (ch == '1')
      {
        softPwmWrite(SERVO, preset[ch2no(ch)-1]);
        pos  = preset[ch2no(ch)-1];
      }
        
      else if(ch == '2')
      {
        softPwmWrite(SERVO, preset[ch2no(ch)-1]);
        pos  = preset[ch2no(ch)-1];
      }
      
      else if(ch == '3')
      {
        softPwmWrite(SERVO, preset[ch2no(ch)-1]);
        pos  = preset[ch2no(ch)-1];
      }
      
      else if(ch == '4')
      {
        softPwmWrite(SERVO, preset[ch2no(ch)-1]);
        pos  = preset[ch2no(ch)-1];
      }
      
      else if(ch == '5')
      {
        softPwmWrite(SERVO, preset[ch2no(ch)-1]);
        pos  = preset[ch2no(ch)-1];
      }
      
      else if(ch == '.')
      {
        if( pos <= MAX - offset )	pos = pos + offset;
        else						          pos = MAX;
        
        softPwmWrite(SERVO, pos);
      }
      
      else if(ch == ',') // SERVO right until pos==MIN
      {
        if( pos >= MIN + offset )	pos = pos - offset;
        else						          pos = MIN;
        
        softPwmWrite(SERVO, pos);
      }
      
      else;
      
      printf("SERVO Position = %2d\n", pos);
    }
    else;
  }
}

int ch2no(unsigned char ch)
{						          // '0' - '0' = 48 - 48 = 0
	int res = ch - '0';	// '1' - '0' = 49 - 48 = 1
	return res;			    // '2' - '0' = 49 - 48 = 2
}						          // '3' - '0' = 50 - 48 = 3