import random as r
import time as t

final_ans = r.randint(1,1000) #ans 1-999
Top = 999
Down = 1

Running = True

t1 = t.time()
t.sleep(1)

while (Running == True):
print("終極密碼, %d ~ %d" %(Down,Top), end=', ')
trynumber = (int)(input("請開始："))
if (trynumber != final_ans):
if ((Down < trynumber < Top) == True):
if (trynumber < final_ans):
Down = trynumber
elif (trynumber > final_ans):
Top = trynumber
else:
print("猜對了! 您共使用了%.6f秒" %(t.time()-t1))
Running = False
