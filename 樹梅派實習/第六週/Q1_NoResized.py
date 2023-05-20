import numpy as np
import cv2
# Load an color image in grayscale
img = cv2.imread('Car.jpeg') #副檔名須一致
#img = cv2.resize(img, (300, 300))
fonts = cv2.FONT_HERSHEY_SIMPLEX


pts1 = np.array([[103, 408], [209, 451], [86, 639], [3, 639], [6, 510]], np.int32)
pts2 = np.array([[372, 493], [532, 539], [492, 636], [303, 636]], np.int32)
pts3 = np.array([[103, 262], [262, 285], [294, 238], [134, 212]], np.int32)
pts4 = np.array([[373, 143], [308, 226], [396, 252], [452, 165]], np.int32)
pts5 = np.array([[540, 179], [504, 275], [602, 291], [622, 202]], np.int32)
pts6 = np.array([[101, 259], [13, 337], [128, 378], [235, 284]], np.int32)

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

cv2.putText(img, "Free", (176,361), fonts, 1, (0,255,0), 2, cv2.LINE_AA)
cv2.putText(img, "Free", (187,423), fonts, 1, (0,255,0), 2, cv2.LINE_AA)
cv2.putText(img, "Free", (405,483), fonts, 1, (0,255,0), 2, cv2.LINE_AA)
cv2.putText(img, "Used", (179,174), fonts, 1, (0,255,255), 2, cv2.LINE_AA)
cv2.putText(img, "Used", (394,113), fonts, 1, (0,255,255), 2, cv2.LINE_AA)
cv2.putText(img, "Used", (565,133), fonts, 1, (0,255,255), 2, cv2.LINE_AA)

def OnMouseAction(event,x,y,flags,param):
  if event == cv2.EVENT_LBUTTONDOWN:
      print("X=",x,",Y=",y)
cv2.namedWindow('image')
cv2.setMouseCallback('image',OnMouseAction)

cv2.imshow('image', img)

cv2.waitKey(0) #等待鍵盤任意鍵
cv2.destroyAllWindows()

