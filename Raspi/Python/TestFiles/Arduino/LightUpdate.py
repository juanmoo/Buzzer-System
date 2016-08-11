#!/usr/bin/python

import time
import smbus

bus = smbus.SMBus(1)
slave_address = 0x10

onArr = []
offArr = []

for x in range(8):
    onArr.append(1)
    offArr.append(0)

while True:
    time.sleep(.5)
    bus.write_i2c_block_data(slave_address,11,onArr)
    time.sleep(.5)
    bus.write_i2c_block_data(slave_address,11,offArr)
