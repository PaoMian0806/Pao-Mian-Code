
import PySimpleGUI as sg
sg.theme('LightBlue2')

# 1. 視窗內容物件布局
layout = [[sg.In('', key='Ans', size=(22,1))],
          [sg.Button('0',key='0'),sg.Button('1',key='1'),
          sg.Button('2',key='2'),sg.Button('3',key='3'),
          sg.Button('4',key='4')],
          [sg.Button('5',key='5'),sg.Button('6',key='6'),
          sg.Button('7',key='7'),sg.Button('8',key='8'),
          sg.Button('9',key='9')],
          [sg.Button('+',key='ADD'), sg.Button('-',key='SUB'),
           sg.Button('*',key='MUL'), sg.Button('/',key='DIV'),
           sg.Button('=',key='EQU')]
]

# 2. 顯示視窗  
window = sg.Window('小算盤', layout)

# 3. 事件處理以及物件的回傳值
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED :
        break
    #如果按下的是0~9       
    if '0' <= event <= '9':
        if values['Ans'] == '0' or values['Ans'] == '':
            window['Ans'].update(event)
            values['Ans'] = event
        else: 
            window['Ans'].update(values['Ans'] + event)
            values['Ans'] = values['Ans'] + event
        print(values)
    elif event == 'ADD':
        NumberA = values['Ans']
        OP = '+'
        window['Ans'].update('')
        values['Ans'] = ''
    elif event == 'SUB':
        NumberA = values['Ans']
        OP = '-'
        window['Ans'].update('')
        values['Ans'] = ''
    elif event == 'MUL':
        NumberA = values['Ans']
        OP = '*'
        window['Ans'].update('')
        values['Ans'] = ''
    elif event == 'DIV':
        NumberA = values['Ans']
        OP = '/'
        window['Ans'].update('')
        values['Ans'] = ''
    elif event == 'EQU':
        if values['Ans'] != '' and NumberA == '':
            reans = float(values['Ans'])
        elif values['Ans'] == '' and NumberA != '':
            reans = float(NumberA)
        else:
            NumberB = values['Ans']
            if OP == '+':
                reans = float(NumberA) + float(NumberB)
            elif OP == '-':
                reans = float(NumberA) - float(NumberB)
            elif OP == '*':
                reans = float(NumberA) * float(NumberB)
            elif OP == '/':
                reans = float(NumberA) / float(NumberB)
                
            NumberA = ''
            NumberB = ''
                
        window['Ans'].update(reans)
        print(reans)

# 4. Close window
window.close()
