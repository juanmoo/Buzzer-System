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

def updateLightState(lightState):
    assert isinstance(lightState, list)
    for state in lightState:
        assert state == 1 or state == 0
    assert len(lightState) == 8
    bus.write_i2c_block_data(arduino_address,11,lightState)
    
