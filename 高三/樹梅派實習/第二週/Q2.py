import random as r

num_list = []
lucky = []

for a in range(1,43):
num_list.append(a)

rnum = r.sample(num_list,7)
#lucky.append(rnum[0]*10 + rnum[1])


print("Number:",end=' ')

for n in range(0,6):
print(rnum[n],end=' ')

print("\nLucky Number:",end=' ')
print(rnum[6],end='')

print("\n")
