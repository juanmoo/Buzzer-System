#include "ShiftIn.h"
#include <math.h>

byte la;
byte da;
byte cl;
static int nums [10];

ShiftIn::ShiftIn(int d, int c, int l) {
  la = l;
  da = d;
  cl = c;

  pinMode(la, OUTPUT);
  pinMode(da, INPUT);
  pinMode(cl, OUTPUT);
}

ShiftIn::~ShiftIn() {

}

void ShiftIn::clk() {
  digitalWrite(cl, 1);
  digitalWrite(cl, 0);
}

void ShiftIn::latch() {
  digitalWrite(la, 1);
  digitalWrite(la, 0);
}

int * ShiftIn::read() {

  latch();
  for(int i  = 0; i<9; i++) {
    nums[i] = digitalRead(da);
    clk();
  }
  return nums;
}

int * ShiftIn::pins() {
  return nums;
}


/*int ShiftIn :: pinsNum() {
  int total = 0;

  for (int i = 0; i<8; i++) {
    total += pins()[i]* (int) (pow(2,7-i)+.3);
  }

  return total;
}*/
