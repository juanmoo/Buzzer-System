#!/usr/bin/python

import smbus
import time

#Initialize IIC buzzState
bus = smbus.SMBus(1)
arduino_address = 0x10

while (True):
    time.sleep(.5)
    data = bus.read_i2c_block_data(arduino_address,0)
    data2 = []
    for x in range(8):
        data2.append(data[x])
    print data2
