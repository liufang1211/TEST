'''
#E1
from __future__ import print_function
def getPentagoalNumber(n):
    for i in range(1,n):
        s = (i*(3*i-1))/2
        print(str(s),"\t",end="")
        if i%10==0:
            print('')
getPentagoalNumber(100)
'''
'''
#E2
def sumDigits(n):
    summ = 0
    cd = len(str(n))
    for i in range(1,cd+1):
        a = n % 10
        n = n //10
        summ = summ +a
    print(summ)
e = eval(raw_input(">>"))
sumDigits(e)

'''
'''
#E3
def displaySortedNumber(num1,num2,num3):
    if num1 > num2:
        num2,num1 = num1,num2
    elif num2 > num3:
        num3,num2 = num2,num3
    elif num1 > num2:
        num2,num1 = num1,num2
    print(num1,num2,num3)
a,b,c = eval(raw_input(">>"))
displaySortedNumber(a,b,c)
'''
'''
#E4
from __future__ import print_function
def p(ch1,ch2,number):
    s = 0
    for i in range(ord(ch1),(ord(ch2)+1)):
        s = s + 1
        print(chr(i),"\t",end="")
        if s%number==0:
            print("")
ch1,ch2 = raw_input(">>")
number = eval(raw_input(">>"))
p(ch1,ch2,number)
'''
'''
#E6
def year(i):
    if i%400==0 | (i%4==0 & i%100!=0):
        print(366)
    else:
        print(365)
for i in range(2010,2021):
year(i)
'''
'''
#E7
import math
def distance(x1,y1,x2,y2):
    s = math.sqrt((x1-x2)**2+(y1-y2)**2)
    print(s)
x1,y1,x2,y2=eval(raw_input(">>>"))
distance(x1,y1,x2,y2)
'''
'''
#E8
def ms(p):
    for i in range(2,p+1):
        for j in range(2,i+1):
            if i%j==0:
                break
        if j == i:
            print(i,2**i-1)
ms(31)
'''
'''
#E9
import time
now=time.localtime(time.time())
print(now[1],now[2],now[0],now[3],":",now[4],":",now[6])
'''
'''
#E10
import random
while 1:
    f = random.randint(1,6)
    s = random.randint(1,6)
    if f+s==2 | f+s==3 | f+s==12:
        print("You rolled"+str(f)+"+"+str(s)+"="+f+s)
        print("You lose")
        break
    elif f+s==7 | f+s==11:
        print("You rolled"+str(f)+"+"+str(s)+"="+f+s)
        print("You win")
        break
    elif f+s==4 | f+s==5 | f+s==6 | f+s==8 | f+s==9 | f+s==10:
        print("you rolled"+str(f)+"+"+str(s)+"="+f+s)
        print("point is"+str(f+s))
        t = random.randint(1,6)
        if t == f+s:
            print("you win")
            break
        elif t == 7:
            print("you lose")
            break

'''

