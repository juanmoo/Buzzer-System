#ifndef ShiftOut_h
#define ShiftOut_h
#include <Arduino.h>

class ShiftOut {
  public:
    ShiftOut(int d, int c, int l);
    ~ShiftOut();
    void write(int bState []);
    void shift(int bState []);
    void latch();
    void clock();
    void data();
    void clear();
};

#endif
