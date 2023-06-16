import numpy as np
import cv2
# Load an color image in grayscale
img = cv2.imread('Ball.jpeg') #副檔名須一致
img = cv2.resize(img, (450, 300))
fonts = cv2.FONT_HERSHEY_SIMPLEX  #字型

cv2.imshow('image', img)

# 高斯 - Blurred

blurred_Img = cv2.GaussianBlur(img, (11, 11), 4)

cv2.imshow('blur_image', blurred_Img)
#cv2.imwrite('blurBall.png', blurred_Img)

# HSV

hsv_Img = cv2.cvtColor(blurred_Img, cv2.COLOR_BGR2HSV)

cv2.imshow('hsv_image', hsv_Img)
#cv2.imwrite('hsvBall.png', hsv_Img)

#  篩選 - Range

RngLower= (74, 0, 0)
RngUpper= (180, 173, 164)
inRange_Img = cv2.inRange(hsv_Img, RngLower, RngUpper)

cv2.imshow('inRange_image', inRange_Img)
#cv2.imwrite('inrangeBall.png', inRange_Img)

# 侵蝕 - Erode

erode_Img= cv2.erode(inRange_Img, None, iterations=1)

cv2.imshow('erode_image', erode_Img)
#cv2.imwrite('erodeBall.png', erode_Img)

# 膨脹 - Dilate

dilate_Img= cv2.dilate(erode_Img, None, iterations=1)

cv2.imshow('dilate_image', dilate_Img)
#cv2.imwrite('dilateBall.png', dilate_Img)

# 輪廓 - Contour

(_ , cnts , _) = cv2.findContours(dilate_Img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#if len(cnts)>0 :
for c in cnts:
    cv2.drawContours(img, [c], 0, (0,255,0), 3)  #將輪廓畫在原圖上
    Area = cv2.contourArea(c)
    print(Area)

M = cv2.moments(c)
centerX = int(M['m10']/M['m00'])
centerY = int(M['m01']/M['m00'])

txt = str(centerX)+ ', ' + str(centerY) #將中心點數字轉成文字
cv2.putText(img, txt ,(centerX, centerY), fonts, 0.5 ,(0,255,255), 2,cv2.LINE_AA)
cv2.putText(img, 'o' ,(centerX, centerY+20), fonts, 0.5 ,(0,255,0), 2,cv2.LINE_AA)

cv2.imshow('contour_image', img)
#cv2.imwrite('contourBall.png', img)

cv2.waitKey(0) #等待鍵盤任意鍵
cv2.destroyAllWindows()

