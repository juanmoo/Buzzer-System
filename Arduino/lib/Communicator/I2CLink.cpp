extern "C" {
  #include <inttypes.h>
  #include <stdlib.h>
}

#include "I2CLink.h"
#include <Arduino.h>

// Initialize Class Variables ///////////////////

uint8_t * (*I2CLink::user_getBuzzState)(void);
uint8_t * (*I2CLink::user_getButtonState)(void);
void (*I2CLink::user_updateLightState)(int *);
int I2CLink::rs;

// Constructors //////////////////////////////////

I2CLink::I2CLink()
{
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  begin();
}


// Public Methods ///////////////////////////////

    // Begin and Stop Methods
    void I2CLink::begin ()
    {
      Wire.begin(slave_address);
    }


    //Setters for user-defined functions
    void I2CLink::onBuzzStateRequest( uint8_t * (*function) (void))
    {
      user_getBuzzState = function;
    }

    void I2CLink::onButtonStateRequest( uint8_t * (*function) (void))
    {
      user_getButtonState = function;
    }

    void I2CLink::onUpdateLightStateRequest(void (*function)(int *))
    {
      user_updateLightState = function;
    }


    //Internal functions
    void I2CLink::receiveData(int byteCount)
    {
      int cmd = Wire.read();

      if (cmd<=10) //Request to read from the Arduino
      {
          readState(cmd);
      }

      else //Request to write to Arduino
      {
        uint8_t data [8];

        if (byteCount>1) //Define data array if data is available
        {
            int index = 0;
            while (Wire.available()>0)
            {
              data[index++] = Wire.read();
            }
        }

        writeState(cmd, &data[0]);
      }

    }

    void I2CLink::readState(int cmd) //cmd <= 10
    {
      rs = cmd;
    }

    void I2CLink::sendData()
    {
      if (rs == 0) // Send Buzzer Data
      {
        const uint8_t * buzzState = user_getBuzzState();
        Wire.write(buzzState,8);
      }

      if (rs == 1) // Send Button data
      {
        const uint8_t * buttonState = user_getButtonState();
        Wire.write(buttonState,8);
      }

      rs = -1;
    }

    void I2CLink::writeState (int cmd, uint8_t * data)
    {
      if (cmd == 11) // write the new lightState to the Arduino
      {
        int lightState[8];
        for (int i = 0; i<8; i++) {
            lightState[i] = data[i];
        }
        user_updateLightState(&lightState[0]);
      }


    }
