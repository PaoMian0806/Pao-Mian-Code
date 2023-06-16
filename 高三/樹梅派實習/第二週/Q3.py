class Myage: #age
def __init__(self,age):
self.age = age
def agekey(self):
if (self.age < 13):
return 'Kid'
elif (self.age < 19):
return 'TeenAge'
elif (self.age < 31):
return 'Young'
else:
return 'Man'

Age = Myage((int)(input("your age=")))
print(Age.agekey())
