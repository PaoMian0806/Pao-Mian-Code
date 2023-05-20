from gpiozero import MCP3208
from time import  sleep

adc = MCP3208(0)
# Vo = -0.0044*LUX + 1.5373
# LUX = (Vo - 1.5373)/(-0.0044)

while True:
        ch0 = adc.value   
        print(ch0)
        # 換算為 0 ~ 3.3v 的電壓值 
        #Vo = ch0 * 3.3
        LUX = ((ch0 * 3.3) - 1.5496)/(-0.0045)
        print('電壓 = %.1f LUX' %LUX)
        sleep(0.5)
