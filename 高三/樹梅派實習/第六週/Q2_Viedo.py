import numpy as np
import cv2
from gpiozero import PWMLED
from time import sleep

ledup = PWMLED(23)
leddown = PWMLED(24)
ledleft = PWMLED(25)
ledright = PWMLED(12)
screenshot = 0;

cap = cv2.VideoCapture(0)
fonts = cv2.FONT_HERSHEY_SIMPLEX  #字型

while True:
    # 1. 取得一張畫面
    ret, img= cap.read()
    #    如果無法取得
    if not ret:
        print("Can't receive frame Exiting ...")
        break
    # 2. 處理 -- 舉例:將畫面轉為灰階 (請改成你的影像處理程序)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  

    # 3. 顯示
    #cv2.imshow('Video', gray)
    # 按鍵q 可以跳出迴圈
    
    blurred_Img = cv2.GaussianBlur(img, (11, 11), 10)

    #cv2.imshow('blur_image', blurred_Img)
    #cv2.imwrite('blurBall.png', blurred_Img)

    # HSV

    hsv_Img = cv2.cvtColor(blurred_Img, cv2.COLOR_BGR2HSV)

    #cv2.imshow('hsv_image', hsv_Img)
    #cv2.imwrite('hsvBall.png', hsv_Img)

    #  篩選 - Range

    RngLower= (84,23,13)
    RngUpper= (156,224,176)
    inRange_Img = cv2.inRange(hsv_Img, RngLower, RngUpper)

    #cv2.imshow('inRange_image', inRange_Img)
    #cv2.imwrite('inrangeBall.png', inRange_Img)

    # 侵蝕 - Erode

    erode_Img= cv2.erode(inRange_Img, None, iterations=3)

    #cv2.imshow('erode_image', erode_Img)
    #cv2.imwrite('erodeBall.png', erode_Img)

    # 膨脹 - Dilate

    dilate_Img= cv2.dilate(erode_Img, None, iterations=1)

    #cv2.imshow('dilate_image', dilate_Img)
    #cv2.imwrite('dilateBall.png', dilate_Img)

    # 輪廓 - Contour

    (_ , cnts , _) = cv2.findContours(dilate_Img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #if len(cnts)>0 :
    for c in cnts:
        cv2.drawContours(img, [c], 0, (0,255,0), 3)  #將輪廓畫在原圖上
        Area = cv2.contourArea(c)
        #print(Area)

    M = cv2.moments(c)
    centerX = int(M['m10']/M['m00'])
    centerY = int(M['m01']/M['m00'])
    
    #320 240
    
    if centerY < 160:
        ledup.value = 1
        leddown.value = 0
    elif centerY > 320:
        ledup.value = 0
        leddown.value = 1
    else:
        ledup.value = 0
        leddown.value = 0
        
    if centerX > 426:
        ledleft.value = 0
        ledright.value = 1
    elif centerX < 213:
        ledleft.value = 1
        ledright.value = 0
    else:
        ledleft.value = 0
        ledright.value = 0
        
    txt = str(centerX)+ ', ' + str(centerY) #將中心點數字轉成文字
    cv2.putText(img, txt ,(centerX, centerY), fonts, 0.5 ,(0,255,255), 2,cv2.LINE_AA)
    cv2.putText(img, 'o' ,(centerX, centerY+20), fonts, 0.5 ,(255,255,0), 2,cv2.LINE_AA)

    cv2.imshow('Video', img)
    
    #640X480
    
    
    #cv2.imwrite('contourBall.png', img)

    if cv2.waitKey(1) == ord('q'):
        break
        
#釋放攝影機與記憶體
cap.release()
cv2.destroyAllWindows()

