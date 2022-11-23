
import PySimpleGUI as sg
from gpiozero import LED
from time import strftime

Relay = LED(21)
Relay.off()

# 1. Layout
layout = [ 
  [sg.Txt("System Time: 12:34:56",key='-time-')]  ,
  [sg.Button('ON',key='-on-',size=(10,2)),
   sg.Button('OFF',key='-off-',size=(10,2)) ] ,
  [sg.Txt('Turn On :'), sg.In(key='min_on'), sg.In(key='sec_on')]  ,
  [sg.Txt('Turn Off :'), sg.In(key='min_off'), sg.In(key='sec_off')]
  ]
 
# 2. Create Window
window = sg.Window('work4', layout)
START_T = 0
STOP_T = 0

# 3. Event loop
while True:
    event, values = window.read(timeout=1000)
    if event == '-on-':
        #按下on鈕後的動作
        print('Setting ON Time Successful !')
        START_T = 1
        print(values)
    elif event == '-off-':
        #按下on鈕後的動作
        print('Setting OFF Time Successful !')
        STOP_T = 1
        
    # 每秒自動觸發
    if event == '__TIMEOUT__':
        window['-time-'].update(strftime('System Time: %H:%M:%S '))
        print(strftime('%H:%M:%S')) #取出系統時間"小時"範例
        
    if START_T == 1:
        if (values['min_on'] + values['sec_on']) == (strftime('%M') + strftime('%S')):
            Relay.value = 1
            print('Relay is ON !')
            START_T = 2
    if STOP_T == 1:
        if (values['min_off'] + values['sec_off']) == (strftime('%M') + strftime('%S')):
            print('Relay is OFF !')
            Relay.value = 0
            STOP_T = 0
        
    if event == sg.WIN_CLOSED :
        break
    
# 4. Close window
window.close()
