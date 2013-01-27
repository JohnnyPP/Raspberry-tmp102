import smbus
import time
bus=smbus.SMBus(1)
address=0x48

def tmp102Read():
        tmp = (bus.read_word_data(address, 0))
        return tmp

def TemperatureConversion():
        val = (LSB << 4)
        val |= (MSB >> 4)
        convertedtemp = val*0.0625
        return convertedtemp

for x in range(30):
        iTmp102 = tmp102Read()
        LSB = iTmp102 % 256
        MSB = iTmp102 / 256
        print('Tmp102 decimal ' + str(iTmp102))
        print('Tmp102 hex ' + str(hex(iTmp102)))
        print('LSB byte ' + str(hex(LSB)))
        print('MSB byte ' + str(hex(MSB)))
        print("%.4f" % TemperatureConversion())
        print
        time.sleep(1)
        
