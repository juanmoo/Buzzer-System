#ifndef ShiftIn_h
#define ShiftIn_h

#include <Arduino.h>

class ShiftIn {
  public:
    ShiftIn(int d, int c, int l);
    ~ShiftIn();
    int * read();
    int * pins();
    void clk();
    void latch();
    int pinsNum();    
};



#endif
