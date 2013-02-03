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
        convertedtemp = val*0.0625+1
        return convertedtemp

def TemperatureConversionNewVersion():
        '''
        #the received tmp102 data must be reordered
        e.g. received data=0x2011 (LSB=0x11, MSB=0x20)
        must be translated to 0x1120. 
        LSB<<8 gives additional 2 nulls 0x1100 now one may combine it with MSB
        reverseddata=LSBtoWord|MSB the returned value is 0x1120
        next reversed data must be shifted by 4 (according to tmp102 documentation)
        finally the result must be multiplied by 0.0625 convertedtemp = reverseddata*0.0625
        '''
        LSBtoWord = (LSB<<8)
        reverseddata = LSBtoWord|MSB
        reverseddata = reverseddata>>4
        convertedtemp = reverseddata*0.0625
        return convertedtemp


for x in range(5):
        iTmp102 = tmp102Read()
        LSB = iTmp102 % 256
        MSB = iTmp102 / 256
        print('Tmp102 decimal ' + str(iTmp102))
        print('Tmp102 hex ' + str(hex(iTmp102)))
        print('LSB byte ' + str(hex(LSB)))
        print('MSB byte ' + str(hex(MSB)))
        print("%.4f" % TemperatureConversion())
        print("%.4f" % TemperatureConversionNewVersion())
        print
        time.sleep(1)
        
