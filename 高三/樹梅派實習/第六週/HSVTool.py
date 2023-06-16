import PySimpleGUI as sg
import numpy as np
import cv2
cap = cv2.VideoCapture(0)

layout = [
[sg.Txt('影像來源'),sg.Radio('File', "src", default=True), sg.Radio('Camera', "src")],
[sg.Txt('File:'), sg.Input('002.jpg',key='filename'), sg.FileBrowse(target='filename'),sg.OK()],
[sg.Image(filename='',key='image'),sg.Image(filename='',key='inRanged')],
[sg.Txt('Lower'), sg.Slider(range=(0, 180),key='H1',enable_events=True),sg.Slider(range=(0, 255),key='S1',enable_events=True),sg.Slider(range=(0, 255),key='V1',enable_events=True),sg.T(' '*30),
sg.Txt('Upper'), sg.Slider(range=(0, 180),default_value=60,key='H2',enable_events=True),sg.Slider(range=(0, 255),default_value=250,key='S2',enable_events=True),sg.Slider(range=(0, 255),default_value=250,key='V2',enable_events=True)],
    ] 
window = sg.Window('inRange Tools', layout)

img = np.zeros((240,320,3), np.uint8)
blurred = cv2.GaussianBlur(img, (7, 7), 0)
hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

while True:
    event, values = window.read(timeout=50)
    #print(event,values)
    
    if event == sg.WIN_CLOSED :
         break
    if event == 'OK':
        img = cv2.imread(values['filename'])
        img = cv2.resize(img, (320, 240))
        blurred = cv2.GaussianBlur(img, (7, 7), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
     
    if event == '__TIMEOUT__':
        if values[1]:
            ret, frame = cap.read()
            img = cv2.resize(frame, (320, 240))
            blurred = cv2.GaussianBlur(img, (7, 7), 0)
            hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        RngLower= (int(values['H1']), int(values['S1']), int(values['V1']))
        RngUpper= (int(values['H2']), int(values['S2']), int(values['V2']))
        inRanged = cv2.inRange(hsv, RngLower, RngUpper)    
        #img to GUI show
        start_img = cv2.imencode('.png', img)[1].tobytes()
        window['image'].update(data=start_img)    
        GUIimg = cv2.imencode('.png', inRanged)[1].tobytes()
        window['inRanged'].update(data=GUIimg)

window.close()
cv2.destroyAllWindows()
