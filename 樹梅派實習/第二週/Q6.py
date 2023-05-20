import random as r

Stop = True

while (Stop == True):
type_list = ['♠','♥']
#type_list = ['♠','♥','♣','♦']
num_list = [9,10,11,12,13]
#num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
Same_num_list = []
CardAns = False
Same = 0
Third = 0
AllFull = 0
AllFullLim = 0

#組合產生52個牌庫
card = [] #定義一個空的list
for t in type_list:
for n in num_list:
card.append(t+str(n))
#print(card)

#用sample的方法抽5張
player1=[]
player1 = r.sample(card,5)
print(player1)


#擷取出字串中的部分
player_Num = []
player_Card = []

for p1 in player1:
player_Num.append(p1[1:])
player_Card.append(p1[0])

#print(player_Card)
#print(player_Num)

#Word = 'abcd1234'
#L1 = Word[3] #取第3個字 ==> d
#L2 = Word[1:3] #取第1~3個字 ==>bc (不包含第3個字)
#L3 = Word[5:] #取第5個字到最後 ==> 234


#判斷牌型
for i in range(9,14): #1,14
#print("%d : %d" %(i,(player_Num.count((str)(i)))))
if (player_Num.count((str)(i)) == 2):
Same+=1
elif (player_Num.count((str)(i)) == 3):
Third+=1
elif (player_Num.count((str)(i)) > 0):
Same_num_list.append(1)
for i in type_list:
#print(i + " : %d" %(player_Card.count(i)))
if (player_Card.count(i) == 5):
CardAns = True

#print("Ans:")

for i in Same_num_list:
AllFull+=i
if (CardAns == True):
if (AllFull == 5):
print("拿到同花順 Straight Flush!")
Stop = False
#else:
#print("拿到同花 Flush!")
#elif (AllFull == 5):
# print("拿到順子 Straight!")
#if ((Third*Same) == 0):
#if (Same > 0):
# print("拿到%d對 %d Pair!" %(Same,Same))
#elif (Third > 0):
#print("拿到3條 Three of the kind!")
#else:
# print("拿到葫蘆 Full House!")

#1. 如果有2張一樣數字的, 顯示"拿到1對!"(20%)
#2. 如果有兩組2張一樣數字的, 顯示"拿到2對!"(20%)
#3. 如果有3張一樣數字的, 顯示"拿到3條!”(20%)
#4. 如果5張一樣花色的, 顯示"拿到同花!"(20%)
#5. 如果有3張一樣及2張一樣的數字, 顯示"拿到葫蘆!" (20%)
