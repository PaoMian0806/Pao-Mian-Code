import numpy as np
import cv2
# Load an color image in grayscale
img = cv2.imread('Car.jpeg') #副檔名須一致
img = cv2.resize(img, (300, 300))
fonts = cv2.FONT_HERSHEY_SIMPLEX


pts1 = np.array([[37, 196], [80, 216], [32, 298], [1, 297], [3, 237]], np.int32)
pts2 = np.array([[138, 233], [202, 255], [185, 299], [114, 297]], np.int32)
pts3 = np.array([[114, 112], [148, 121], [167, 77], [138, 70]], np.int32)
pts4 = np.array([[188, 128], [227, 138], [232, 92], [202, 87]], np.int32)
pts5 = np.array([[106, 113], [90, 134], [36, 124], [54, 99]], np.int32)
pts6 = np.array([[34, 131], [9, 157], [45, 172], [87, 138]], np.int32)

pts1 = pts1.reshape((-1, 1, 2))
pts2 = pts2.reshape((-1, 1, 2))
pts3 = pts3.reshape((-1, 1, 2))
pts4 = pts4.reshape((-1, 1, 2))
pts5 = pts5.reshape((-1, 1, 2))
pts6 = pts6.reshape((-1, 1, 2))

#cv2.rectangle(img,(120,135),(210,220),(255,0,0),3) #左上座標跟右下座標
#cv2.putText(img, "Face", (120,105), fonts, 1, (255,0,0), 2, cv2.LINE_AA) #LINE_AA =  反鋸齒反鋸齒,  座標以左下角為主

cv2.polylines(img, [pts1], True, (0, 255, 0), 3)
cv2.polylines(img, [pts2], True, (0, 255, 0), 3)
cv2.polylines(img, [pts3], True, (0, 255, 255), 3)
cv2.polylines(img, [pts4], True, (0, 255, 255), 3)
cv2.polylines(img, [pts5], True, (0, 255, 255), 3)
cv2.polylines(img, [pts6], True, (0, 255, 0), 3)

cv2.putText(img, "Free", (49,188), fonts, 0.7, (0,255,0), 2, cv2.LINE_AA)
cv2.putText(img, "Free", (151,222), fonts, 0.7, (0,255,0), 2, cv2.LINE_AA)
cv2.putText(img, "Free", (97,152), fonts, 0.7, (0,255,0), 2, cv2.LINE_AA)
cv2.putText(img, "Used", (25,76), fonts, 0.7, (0,255,255), 2, cv2.LINE_AA)
cv2.putText(img, "Used", (129,51), fonts, 0.7, (0,255,255), 2, cv2.LINE_AA)
cv2.putText(img, "Used", (199,59), fonts, 0.7, (0,255,255), 2, cv2.LINE_AA)

def OnMouseAction(event,x,y,flags,param):
  if event == cv2.EVENT_LBUTTONDOWN:
      print("X=",x,",Y=",y)
cv2.namedWindow('image')
cv2.setMouseCallback('image',OnMouseAction)

cv2.imshow('image', img)

cv2.waitKey(0) #等待鍵盤任意鍵
cv2.destroyAllWindows()

