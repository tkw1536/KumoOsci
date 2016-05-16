#include <avr/io.h> 

#include <avr/interrupt.h> 

// initialize timer, interrupt and variable 

void timer1_init() 

{ 
// set up timer with prescaler = 256 and CTC mode 
TCCR1A|= (1 << WGM12)|(1 << CS12); 
TCNT1 = 0; // initialize counter 
OCR1A =31249; // initialize compare value 
TIMSK1 |= (1 << OCIE1A); // enable compare interrupt 
sei(); //enable global interrupts 
} 
// ISR is fired whenever a match occurs to toggle and blink led 
ISR (TIMER1_COMPA_vect){ 
PORTD ^= _BV(PD3); 
} 
int main(void) 
{ 
DDRD |=_BV(PD3); // connect led to pin PD3 
timer1_init(); // initialize timer 
while(1) // loop forever 
{ 
} 
} 

