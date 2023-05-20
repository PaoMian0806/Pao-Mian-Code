import math
import PySimpleGUI as sg
sg.theme('LightBlue2')
# 1. 視窗內容物件布局
layout = [ [sg.Text('A數:'), sg.InputText(key = 'numA')],
           [sg.Text('運算:'),
            sg.Combo(['加', '減', '乘', '除', '次方', '根號'],
                     key = 'sgfunc', size = (5, 1))],
            [sg.Text('B數:'), sg.InputText(key = 'numB')],
            [sg.Text('Ans:'), sg.Text(key = 'Ans', size = (20, 1))],
            [sg.Button('計算')]
           ]
 
# 2. 顯示視窗  
window = sg.Window('簡易計算器', layout)
 
# 3. 事件處理以及物件的回傳值
while True:
   event, values = window.read()
   
   
   if event == sg.WIN_CLOSED:
        break
   elif event == '計算':
       if values['sgfunc'] == '加':
           reans = int(values['numA']) + int(values['numB'])
       elif values['sgfunc'] == '減':
           reans = int(values['numA']) - int(values['numB'])
       elif values['sgfunc'] == '乘':
           reans = int(values['numA']) * int(values['numB'])
       elif values['sgfunc'] == '除':
           reans = int(values['numA']) / int(values['numB'])
       elif values['sgfunc'] == '次方':
           if values['numA'] == '' and values['numB'] == '':
               reans = 'ERROR'
           elif values['numA'] != '':
               reans = pow(int(values['numA']),2)
           elif values['numB'] != '':
               reans = pow(int(values['numB']),2)
       elif values['sgfunc'] == '根號':
           if values['numA'] == '' and values['numB'] == '':
               reans = 'ERROR'
           elif values['numA'] != '':
               reans = math.sqrt(int(values['numA']))
           elif values['numB'] != '':
               reans = math.sqrt(int(values['numB']))
           
       window['Ans'].update(reans)
       
       print(values)
       print(reans)

# 4. Close window
window.close()
