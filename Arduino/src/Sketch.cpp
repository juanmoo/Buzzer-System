#include <Arduino.h>
#include <I2CLink.h>
#include <ShiftIn.h>
#include <ShiftOut.h>
#include <Adafruit_LEDBackpack.h>
#include <Adafruit_GFX.h>

//Instantinate Global Objects
Adafruit_7segment timeDisplay = Adafruit_7segment();
I2CLink linker = I2CLink();
ShiftIn reader = ShiftIn(4,2,3); //ShiftIn(data pin, clock pin, latch pin)
ShiftOut shifter = ShiftOut(16,14,15); //ShiftOut(data pin, clock pin, latch pin)

//Initializing functions to be implemented later
uint8_t * sendBuzzState (void);
uint8_t * sendButtonState (void);
void updateLightState (int *);
void displayNumber(uint16_t);

//Initializing global Variables
uint8_t buzzState [8];
uint8_t buttonState [8];


void setup()
{
    //Setup I2C linker
    linker.begin();
    linker.onButtonStateRequest(sendButtonState);
    linker.onBuzzStateRequest(sendBuzzState);
    linker.onUpdateLightStateRequest(updateLightState);

    //Set Pinmode for button Pins
    for (int i = 5; i<=12; i++)
    {
      pinMode(i, INPUT);
    }

    //Start Serial Port
    Serial.begin(9600);
    while (!Serial);
    delay(100);
    Serial.println("READY TO BEGIN!\n\n");
}

void loop()
{
  delay(10);
}

uint8_t * sendBuzzState ()
{
  int * h = reader.read();
  for (int i = 0; i<8; i++)
  {
    buzzState[i] = h[i];
  }

  return &buzzState[0];
}

uint8_t * sendButtonState ()
{
  for (int i = 0; i<8; i++)
  {
    buttonState[i] = digitalRead(i+5);
  }
  return &buttonState[0];
}

void updateLightState (int * lightState)
{
  shifter.write(lightState);
}

// 7-Segment Display Functions /////////////

void displayNumber (uint16_t time_s)
{
  // Set address of 7-segment
  Wire.endTransmission(true);
  timeDisplay.begin(0x70);

  timeDisplay.writeDigitNum(0,time_s/60/10,false);
  timeDisplay.writeDigitNum(1, (time_s/60)%10, false);
  timeDisplay.drawColon(true);
  timeDisplay.writeDigitNum(3, (time_s%60)/10, false);
  timeDisplay.writeDigitNum(4, (time_s%60)%10, false);
  timeDisplay.writeDisplay();

  // Restart linker
  linker.begin();
}
