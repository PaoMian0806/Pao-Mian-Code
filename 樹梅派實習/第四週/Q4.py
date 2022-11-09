from gpiozero import DistanceSensor, PWMLED, TonalBuzzer
from signal import pause
from time import sleep
from gpiozero.tones import Tone

spk = TonalBuzzer(21) # change pin 

sensor = DistanceSensor(27, 17) #(Echo, Trig)

while True:
    D = 100 * sensor.distance
    print('%.2fcm' %D)
    if D < 15:
        spk.play("C4")
    elif D < 30:
        spk.play("C4")
        sleep(0.4)
        spk.stop()
        sleep(0.4)
    elif D < 50:
        spk.play("C4")
        sleep(0.5)
        spk.stop()
        sleep(0.5)
    else:
        spk.play("C4")
        sleep(1)
        spk.stop()
        sleep(1)
