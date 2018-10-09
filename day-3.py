'''
#E1
a = 0
b = 0
c = 0
su= 0
num = eval(raw_input(">>"))
while num == 0:
    print("error")
    break
while num != 0:
    if num > 0:
        a+=1
    elif num < 0:
        b+=1
    num = eval(raw_input(">>"))
    su = num+su
    c = a +b
print("zheng shu have :"+str(a))
print("fu shu have :"+str(b))
print("ping jun shu is:" + str(su / c))
'''

'''
#E2
rate = 0.05
fee =10000
su=0
su1=0
for i in range (10):
    fee = fee * (rate+ 1)
    su = su+fee
print(su)
for i in range (4):
    su = su * (rate + 1)
    su1 = su1 + su
print(su1)
'''

'''
#E4
j = 0
for i in range (100,1000):
    if (i%5==0) and (i%6==0):
        print(i,end=" ")
        j+=1
        if(j%10==0):
            print(" ")
    else :
        i+=1
'''
'''
#E5
n = 1
m=12000
while n*n<=12000:
   n+=1
print(n)
while m*m*m >=12000:
    m=m-1
print(m)
'''
'''
#E6
amount = eval(raw_input("Loan Amount:>>"))
year = eval(raw_input("Number of Years:>>"))
rate = 0.05
while rate <= 0.08:
    Mon_pay =amount * rate_
    rate_=0.05 +(1/8)
    print(rate)

'''

'''
#E7
a = 1.0
n=1.0
sum1 = 0.0
while n<=50000:
    sum1= sum1+a/n
    n+=1
print(sum1)
'''
'''
a = 1.0
sum2= 0.0
n=50000.0
while n>0:
    sum2 = sum2 +a/n
    n=n-1
print(sum2)
'''
'''
#E8
a =1.0
b = 3.0
x=0.0
while b<=99:
    x = a/b + x
    a= a+2
    b= b+2
print(x)
'''
'''
#E9
a = 1.0
sum_=0.0
x=1.0
i = eval(raw_input("i ="))
while x<=i:
    p=((-1)**(x+1))/(2*x-1)
    x+=1
    sum_=sum_+p
sum_=4*sum_
print(sum_)
'''

'''
#E10
for i in range (1,10001):
    sum_=0
    for j in range (1,(i/2+1)):
        if i%j==0:
            sum_ = sum_ + j
    if sum_==i:
        print (sum_)
'''
'''
#E11
sum=0
for i in range (1,8):
    for j in range (i+1,8):
        print(i,j)
        sum+=1
print("The total number of all combinations is "+str(sum))
'''















