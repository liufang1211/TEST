'''
a = 'abcde'
i = 0
while i < len(a):
    print(a[i])
    i+=1


import random
a = eval(raw_input(">>"))
b = random.randint(0,5)
print(b)
while a!=b:
    if a>b:
        print("big")
    elif a<b:
        print("small")
    a = eval(raw_input(">>"))
while a==b:
    print("yes")
    break


sum = 0
i=0
while i<1001:
    sum=sum+i
    i+=1
print(sum)



i=1
for sum in range(10000):
    sum =sum + i
    i+=1
    print(i)
print(sum)



from __future__ import print_function
sum = 0
for i in range (1,10):
    for j in range (1,i+1):
        sum = i * j
        print (str(i)+"*"+str(j)+"="+str(sum))
    print()
''' 

def fun1(num1,num2,num3):
    return num1,num2,num3
def fun2(num1,num2,num3):
    a = num1**2
    b = num2**2
    c = num3**2
    print(a,b,c)
    return a,b,c
def fun3(a,b,c,num1,num2,num3):
    res1 = a -num1
    res2 = b- num2 
    res3 = c- num3
    print(res1,res2,res3)
num1,num2,num3 = fun1(0,1,2)
x,y,z = fun2(num1,num2,num3)
fun3(num1,num2,num3,x,y,z)
    























