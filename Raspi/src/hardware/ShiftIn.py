#Use the functions in this module to check whether or not each buzzer is pressed.
import json
import smbus

try:
    configurationFile = open('hardware/configuration.config')
    configText = configurationFile.read()
except IOError:
    raise IOError('Bad Configuration File')


config = json.loads(configText)
arduino_address = int(config['arduino_address'])
bus = smbus.SMBus(1)



def getBuzzerState():
    data = bus.read_i2c_block_data(arduino_address, 0)
    data2 = []
    for x in range(8):
        data2.append(data[x])
    return data2
