for i in range(1,10): #9x9
for j in range(1,10):
msg = '| {:^2} * {} = {:^2} |'.format(i, j, i*j)
print (msg,end="\n")
