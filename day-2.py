'''
#E1
import math
r = eval(raw_input("Enter the length form the center to a vertex:>>"))
s = 2 * r * math.sin(math.pi/5)
area = 5 * s * s / (4 * math.tan(math.pi/5))
area = round(area,2)
print(area)
'''


'''
#E2
import math
r = 6371.01
x1,y1 = eval(raw_input("Enter point 1(latitude and longitude) in degrees:>>"))
x2,y2 = eval(raw_input("Enter point 2(latitude and longitude) in degrees:>>"))
a = math.sin(math.radians(x1)) 
b = math.sin(math.radians(x2))
c = math.cos(math.radians(x1))
m = math.cos(math.radians(x2))
n = math.cos(math.radians(y1) - math.radians(y2))
d = r * math.acos(a * b + c * m *n)
print(d)
'''


'''
#E3
import math
s = eval(raw_input("Enter the side : >>"))
area = (5 * s * s )/ (4 * math.tan(math.pi/5))
print(area)
'''


'''
#E4
import math
num = eval(raw_input("Enter the number of sides :>>"))
s = eval(raw_input("Enter the side:>>"))
area = (num * s * s) / (4 * math.tan(math.pi/num))
print(area)
'''


'''
#E5
num = eval(raw_input("Enter an ASCII code:>>"))
print(chr(num))
''' 


'''
#E6
name = str(raw_input("Enter employee's name:>>"))
mhours = eval(raw_input("enter number of hours worked in a week:>>"))
pay = eval(raw_input("enter hourly pay rate:>>"))
fed_tax_rate = eval(raw_input("enter federal tax withholding rate:>>"))
sta_tax_rate = eval(raw_input("enter state tax withholding rate:>>"))
gross_pay = pay * hours
federal = gross_pay * fed_tax_rate
state = gross_pay * sta_tax_rate
total = federal + state
net_pay = gross_pay - total
print("employee name:" + name)
print("hours worded:" + str(hours))
print("pay rate:" + str(pay))
print("gross pay:" + str(gross_pay))
print("deductions:")
print("\tfederal (" + str(fed_tax_rate * 100) + "%):" + str(federal))
print("\tstate (" +str(sta_tax_rate * 100) + "%):" + str(state))
print("\ttotal deduction:" + str(total))
print("net pay" + str(net_pay))
'''

'''
#E7
num1 = eval(raw_input("enter an integer :>>"))
a = num1 / 1000
b = (num1 - a *1000 ) / 100
c = (num1 - a * 1000 - b * 100 ) / 10
d = num1 - (a * 1000 + b * 100 + c * 10)
num2 = d * 1000 + c * 100 + b * 10 + a
print(num2)
'''


'''
#E8
''' 


'''
#E9
import math
a, b, c = eval(raw_input("enter a,b,c:>>"))
x = b*b - 4*a*c
if x > 0:
    r1 = (-b + math.sqrt(x)) / 2*a
    r2 = (-b + math.sqrt(x)) / 2*a
    print("the root are " + str(r1) + " and " + str(r2))
elif x == 0:
    r = (-b + math.sqrt(x)) / 2*a
    print("the root is " + str(int(r)))
elif x < 0:
    print("the equation has no real roots")
'''


'''
#E10
import random
num = eval(raw_input("the sum of numbers is :>>"))
a = random.randint(0,100)
b = random.randint(0,100)
sum = a + b
if num == sum:
    print("true")
else :
    print("false")
'''

'''
#E11
today = eval(raw_input("enter today's day:>>"))
num = eval(raw_input("enter the number days elapsed since today:>>"))
today = num % 7 + today
if today == 1:
    print("monday")
elif today == 2:
    print("tuseday")
elif today == 3:
    print("wednesday")
elif today == 4:
    print("thursday")
elif today == 5:
    print("friday")
elif today == 6:
    print("saturday")
elif today == 0:
    print("sunday")
'''


'''
#E12
import math
a,b,c = eval(raw_input("enter three numbers:>>"))
if a > b:
    b = a
elif b > c:
    c = b
elif a > b:
    
    b = a
print (c,a,b)
'''


'''
#E13
w1,p1 = eval(raw_input("Enter weight and price package 1:>>"))
w2,p2 = eval(raw_input("Enter weight and price package 2:>>"))
x1 = w1 / p1
x2 = w2 / p2
if x1 > x2:
    print("Package 1 has the better price")
else :
    print("Package 2 has the better price")
'''


'''
#E14
month = eval(raw_input("Enter the month is :>>"))
year = eval(raw_input("Enter the year is :>>"))
if month == 1,3,5,7,8,10,12:
    print(str(year) + " year " + str(month) + "month have 31 days")
elif month == 4,6,9,11:
    print(str(year) + " year " + str(month) + "month have 30 days")
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(str(year) + " year 2 month have 29 days")
'''


'''
#E15
import random
str1 = eval(raw_input(">>"))
str2 = random.randrange(0,2)
print(str2)
if str1 == str2:
    print("right")
else :
    print("wrong")
'''


'''
#E16
import random
a = eval(raw_input("scissor(0), rock(1), paper(2):>>"))
b = random.randrange(0,3)

if abs(a - b == 1): 
    print("You won")
elif abs(a - b == 2):
    print("You lose")
elif a == b:
    print("It is a draw")
'''


'''
#E17
'''








