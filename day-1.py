'''
#E1
C=float(raw_input("<<"))
F=float((9.0 / 5.0) * C + 32)
print(F)
'''
'''
#E2
radius,length = eval(raw_input(">>"))
area = radius * radius * 3.14
volume = area * length
print(area,volume)
'''
'''
#E3
feet = eval(raw_input("<<"))
meter = feet * 0.305
print(meter)
'''
'''
#E4
M = eval(raw_input("Enter the amount of water in kilograms:>>"))
init_temp = eval(raw_input("Enter the initial temperature:>>"))
final_temp = eval(raw_input("Enter the final temperature:>>"))
Q = M * (final_temp - init_temp) * 4184
print(Q)
'''
'''
#E5
balance,rate = eval(raw_input("Enter balance and interest rate:>>"))
interest = balance * (rate / 1200)
print(interest)
'''
'''
#E6
v0,v1,t = eval(raw_input("Enter v0,v1 and t :>>"))
a = (v1 - v0) / t
print(a)
'''
'''
#E7
amount = eval(raw_input("Enter the
monthly saving amount:>>"))
s=0
for i in range (6):
    amount = amount *(1 + 0.00417)
    s=s+amount
print(s)
'''
'''
#E8
number = eval(raw_input("Enter a number 0 and 999 :>>"))
a = number / 100
b = (number - 100 * a)/ 10
c = number - a * 100 - b * 10
print(a + b + c)
'''
