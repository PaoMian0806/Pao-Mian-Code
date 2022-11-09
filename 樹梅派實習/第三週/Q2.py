from gpiozero import LEDBoard
from gpiozero import PWMLED
from time import sleep


leds = LEDBoard(5, 6, 13, 19, 26, 20)
test = 1

if test == 1 :
    while True:
        leds.value = (0, 0, 1, 1, 0, 0)
        sleep(5)
        for i in range(0,4):
            leds.value = (0, 0, 1, 1, 0, 0)
            sleep(0.5)
            leds.value = (0, 0, 1, 0, 0, 0)
            sleep(0.5)
        leds.value = (0, 0, 1, 0, 1, 0)
        sleep(2)
        leds.value = (1, 0, 0, 0, 0, 1)
        sleep(5)
        for i in range(0,4):
            leds.value = (1, 0, 0, 0, 0, 1)
            sleep(0.5)
            leds.value = (0, 0, 0, 0, 0, 1)
            sleep(0.5)
        leds.value = (0, 1, 0, 0, 0, 1)
        sleep(2)
elif test == 2:
    led = PWMLED(17)
    while True:
        led.value = 0  # off
        sleep(1)
        led.value = 0.5  # half brightness
        sleep(1)
        led.value = 1  # full brightness
        sleep(1)
elif test == 3:
    led = PWMLED(17)
    led1 = PWMLED(27)
    while True:
        for i in range(0,100):
          led.value = i*0.01
          led1.value = 1 - (i*0.01)
          sleep(0.01)

        for i in range(100,0,-1):
          led.value = i*0.01
          led1.value = 1 - (i*0.01)
          sleep(0.01)
elif test == 4:
    led = PWMLED(17)
    led1 = PWMLED(27)
    led2 = PWMLED(22)
    led3 = PWMLED(12)
    led4 = PWMLED(16)
    led5 = PWMLED(25)
    led6 = PWMLED(24)
    led7 = PWMLED(23)
    led8 = PWMLED(18)
    led9 = PWMLED(4)
    while True:
            led.pulse(0.1, 1, 1)
            led1.pulse(0.1, 0.2, 1)
            led2.pulse(0.1, 0.3, 1)
            led3.pulse(0.1, 0.4, 1)
            led4.pulse(0.1, 0.5, 1)
            led5.pulse(0.1, 0.6, 1)
            led6.pulse(0.1, 0.7, 1)
            led7.pulse(0.1, 0.8, 1)
            led8.pulse(0.1, 0.9, 1)
            led9.pulse(0.1, 1, 1)
