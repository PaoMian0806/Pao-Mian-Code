from gpiozero import MCP3208
from time import  sleep

adc = MCP3208(0)

while True:
        ch0 = adc.value   
        print(ch0)
        # 換算為 0 ~ 3.3v 的電壓值 
        Vo = ch0 *3.3
        print('電壓 = %.1f v' %Vo)
        sleep(0.5)
