// ---------------------------------------------------------------------------
#include <Servo.h>
// ---------------------------------------------------------------------------
// Customize here pulse lengths as needed
#define MIN_PULSE_LENGTH 1000 // Minimum pulse length in µs
#define MAX_PULSE_LENGTH 2000 // Maximum pulse length in µs
// ---------------------------------------------------------------------------
Servo motA, motB, motC, motD;
String data, motorData;
char tempData;
int motorValue;
// ---------------------------------------------------------------------------

void setup() {
    Serial.begin(9600);   
    
    delay(1000);
    delay(1000);
    displayInstructions();
}

// Main loop, uses a buffer array to ensure that it doesn't get overloaded. 
char cmdbuf[20];
int n = 0;
void loop() {
    if (Serial.available()) {
        int rd = Serial.read();
        if (rd > 0)
        {
          if (rd == 'i') // Change if different end command is wanted
          {
            String s(cmdbuf); 
             process_cmd(s);
             n = 0;
             cmdbuf[n] = 0;
          }
          else if(n < sizeof(cmdbuf) - 1)
          {
            Serial.println("I am adding the char to the buffer");
            cmdbuf[n++] = rd;
            cmdbuf[n] = 0;
          }
          else
          {
             n = 0;
             cmdbuf[n] = 0;
          }
        }
    }
}
  
void process_cmd(String data){
        tempData = data[0];
        data.remove(0,1);
        switch (tempData) {
            // 0
            case 48 : Serial.println("Running start PWM function");
                     motA.attach(9, MIN_PULSE_LENGTH, MAX_PULSE_LENGTH);
                     motB.attach(11, MIN_PULSE_LENGTH, MAX_PULSE_LENGTH);
            break;
            // 4
            case 49: Serial.println("Setting first motor to your input value");
                     motorValue = data.toInt();
                     motA.writeMicroseconds(motorValue);
            break;
            //5
            case 50: Serial.println("Setting second motor to your input value");
                     motorValue = data.toInt();
                     motB.writeMicroseconds(motorValue);
            break;                  
        }
}

void displayInstructions()
{  
    Serial.println("READY - PLEASE SEND INSTRUCTIONS AS FOLLOWING :");
    Serial.println("\t0 : Start PWM signals");
    Serial.println("\t1 : Set motor 1 to 1100-1900 micro seconds");
    Serial.println("\t2 : Set motor 2 to 1100-1900 micro seconds");
    Serial.println(" Finish each command with an 'i'");
}
