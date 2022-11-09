#https://github.com/Aorda/USSR-Anthem-with-Arduino-Piezo-Buzzer/blob/master/sovietanthem.ino
#http://yhhuang1966.blogspot.com/2016/09/arduino_17.html

from gpiozero import PWMLED, Button, TonalBuzzer
from signal import pause
from time import sleep
from gpiozero.tones import Tone


song1 = ["G4", "C5", "G4", "A4", "B4", "E4", "E4",
         "A4", "G4", "F4", "G4", "C4", "C4", "D4", "D4",
         "E4", "F4", "F4", "G4", "A4", "B4", "C5", "D5","E5",
         "D5", "C5", "D5", "B4", "G4", "C5", "B4", "A4", "B4",
         "E4", "E4", "A4", "G4", "F4", "G4", "C4", "C4", "C5",
         "B4", "A4", "G4", "B4", "C5", "D5", "E5", "D5", "C5",
         "B4", "C5", "D5", "G4", "G4", "B4", "C5", "D5","C5", "B4",
         "A4", "G4", "A4", "B4", "E4", "E4", "G4", "A4", "B4","C5",
         "A4", "B4", "C5", "A4", "B4", "C5", "A4", "C5", "F5","F5",
         "E5", "D5", "C5", "D5", "E5", "C5", "C5","D5", "C5", "B4",
         "A4", "B4", "C5", "A4", "A4","C5", "B4", "A4", "G4", "C4",
         "G4", "A4", "B4", "C5"]

song2 = ["G5", "E5", "E5", "-", "F5", "D5", "D5", "-", "C5", "D5", "E5", "F5", "G5", "G5", "G5", "-",
         "G5", "E5", "E5", "-", "F5", "D5", "D5", "-", "C5", "E5",
         "G5", "G5", "E5", "-", "-", "-","D5", "D5", "D5", "D5", "D5",
         "E5", "F5", "-", "E5", "E5", "E5", "E5", "E5", "F5", "G5",
         "-", "G5", "E5", "E5", "-", "F5", "D5", "D5", "-", "C5", "E5",
         "G5", "G5", "C5", "-", "-", "-"]

noteDurations2 = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

noteDurations1 = [8, 4, 6, 16, 4, 8, 8, 4, 6, 16, 4, 8, 8,
                 4, 8, 8, 4, 8, 8, 4, 8, 8, 2,4, 6, 16, 4,
                 8, 8, 4, 6, 16, 4, 8, 8, 4, 6, 16, 4, 6, 16,
                 4, 6, 16, 8, 8, 8, 8, 2, 8, 8, 8, 8, 3, 8, 8, 8, 8, 8,
                 2, 8, 8, 8, 8, 3, 8, 8, 8, 8, 8,4, 6, 16, 4, 6, 16, 4,
                 8, 8, 2,2, 8, 8, 8, 8, 3, 8, 2,2, 8, 8, 8, 8, 3, 8, 2,
                 4, 6, 16, 4, 4, 2, 4, 4, 1]

spk = TonalBuzzer(22) # change pin 
button = Button(20)
button2 = Button(16)


while True:
     count = 0
     if button.is_pressed:
         for s in song1: #ussr use 2000
             noteDuration = (int)(2000 / (noteDurations1[count])) 
             if s != "-":
                 spk.play(s)
             pauseBetweenNotes = (float)((noteDuration*(1.30))/1000)
             sleep(pauseBetweenNotes)
             spk.stop()
             count+=1
         sleep(0.05)
     elif button2.is_pressed:
         for s in song2: #furelise use 1000
             noteDuration = (int)(1000 / (noteDurations2[count]))
             if s != "-":
                 spk.play(s)
             pauseBetweenNotes = (float)((noteDuration*(1.30))/1000)
             sleep(pauseBetweenNotes)
             spk.stop()
             count+=1
         sleep(0.05)
