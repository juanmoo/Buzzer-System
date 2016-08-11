#ifndef I2CLink_h
#define I2CLink_h

#include <inttypes.h>
#include <Wire.h>

#define slave_address 0x10

/*
* To use this class the following functions need to be implemented:
*   1. onBuzzStateRequest(function) //Sets behavior to get the state of the buzzers.
*   2. onButtonStateRequest(function) //Sets behavior to get the state of the buttons.
*   3. onUpdateLightStateRequest(function) //Sets the method to update the buzzer lights.
*   4. onUpdateTimeRequest(function) //Sets time to be displayed on timer.
*/

class I2CLink
{
  private:
    //Fields
    static int rs;

    //Pointers to user-defined functions
    static uint8_t * (*user_getBuzzState)(void);
    static uint8_t * (*user_getButtonState)(void);
    static void (*user_updateLightState)(int *);

    //Internal functions
    static void receiveData (int);
    static void sendData (void);

    static void readState (int);
    static void writeState (int, uint8_t *);


  public:
    I2CLink();
    void begin();

    void onBuzzStateRequest( uint8_t * (*)(void) );
    void onButtonStateRequest( uint8_t * (*)(void) );
    void onUpdateLightStateRequest( void (*) (int *) );

};

#endif
