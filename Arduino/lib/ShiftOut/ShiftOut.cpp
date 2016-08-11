#include "ShiftOut.h"

byte dat;
byte clk;
byte lat;
boolean dataOn = false;

ShiftOut::ShiftOut(int d, int c, int l) {
  dat =  d;
  clk = c;
  lat = l;
  pinMode(dat, OUTPUT);
  pinMode(clk, OUTPUT);
  pinMode(lat, OUTPUT);
  digitalWrite(dat, 0);
  digitalWrite(clk, 0);
  digitalWrite(lat, 0);
}

ShiftOut::~ShiftOut() {

}

void ShiftOut::latch() {
  digitalWrite(lat, 1);
  digitalWrite(lat, 0);
}

void ShiftOut::clock() {
  digitalWrite(clk, 1);
  digitalWrite(clk, 0);
}

void ShiftOut:: data() {
  if( dataOn ) {
    digitalWrite(dat, 0);
    dataOn = false;
  }
  else {
    digitalWrite(dat, 1);
    dataOn = true;
  }
  
}

void ShiftOut::shift(int bState []) {
  boolean dataOn = false;
  digitalWrite(dat, 0);

  for (int i = 15; i>=0; i--) {
    if(bState[i] == 1) {
      data();
      clock();
      data();
    }
    else {
      clock();
    }
  } 
}

void ShiftOut::write(int bState []) {
  shift(bState);
  latch();
}

void ShiftOut::clear() {
  int state [16] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
  write(state);
}
