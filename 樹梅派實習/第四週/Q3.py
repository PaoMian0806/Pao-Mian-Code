from gpiozero import MCP3208
from time import  sleep

adc = MCP3208(0)


while True:
        ch0 = adc.value
        temp = ch0 * 100
        print('temp = %.2f C' %temp)
        sleep(0.5)
