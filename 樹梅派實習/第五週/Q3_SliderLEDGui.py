import PySimpleGUI as sg
from gpiozero import PWMLED
from time import sleep

sg.theme('LightBlue2')

Led_R = PWMLED(16)
Led_G = PWMLED(20)
Led_B = PWMLED(21)

layout = [  [ sg.Slider(range=(0, 100),key='R'),
              sg.Slider(range=(0, 100),key='G'),
              sg.Slider(range=(0, 100),key='B') ],
            [sg.Button('Submit'),sg.Button('Rainbow')] ]

window = sg.Window('LED', layout)

# 3. 事件處理以及物件的回傳值
while True:
    event, values = window.read(timeout = 100)
    if event == sg.WIN_CLOSED :
        break
    if event == 'Submit':
        Led_R.value = values['R'] / 100
        Led_G.value = values['G'] / 100
        Led_B.value = values['B'] / 100
        print(values)
    elif event == 'Rainbow':
        
        Led_R.value = 0
        Led_G.value = 0
        Led_B.value = 0
        
        for i in range(0,255):
          Led_R.value = i/255
          sleep(0.01)
        for i in range(0,255):
          Led_G.value = i/255
          sleep(0.01)
        for i in range(255,0,-1):
          Led_R.value = i/255
          sleep(0.01)
        for i in range(0,255):
          Led_B.value = i/255
          sleep(0.01)
        for i in range(255,0,-1):
          Led_G.value = i/255
          sleep(0.01)
        for i in range(255,0,-1):
          Led_B.value = i/255
          sleep(0.01)
  
# 4. Close window
window.close()
