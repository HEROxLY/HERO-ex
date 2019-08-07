import os
os.system ('clear') 

A = '\033[1;31m'
B = '\033[1;32m'
C = '\033[1;33m'
print (A)
name = input ('enter name===> ')
print (B)
email = input ('enter email===> ')
number = 1949
while number<2100:
    number=number+1
    print (C)
    print(name+str(number)+email)
print('email extraction done')