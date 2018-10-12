'''
#E1
def len(a):
    if a[0:3].isdigit()==True and a[4:6].isdigit()==True and a[7:11]==True:
        print 'Vaild SSN'
    else:
        print 'Invaild SSN'
a=raw_input('Enter a number as ddd-dd-dddd:')
len(a)
'''

'''
#E2
def find():
    if a in b:
        print 'yes'
    else:
        print 'no'
a=str(raw_input('Enter a string:'))
b=str(raw_input('Enter a string:'))
find()
'''
'''
#E3
def m(a):
    count=0
    sum=0
    for i in a:
        count+=1
        if ord(i)>=48 and ord(i)<=57:
            sum+=1
    if count >=8 and a.isalnum()==True and sum>=2 :
        print ('vaild password')
    else:
        print ('invaild password')
a=str(raw_input('>>>'))
m(a)
'''
'''
#E4
def countLetters(a):
    count=0
    for i in a:
        if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
            count+=1
    print count
a=str(raw_input('>>>'))
countLetters(a)
'''
'''
#E5
def getNumber(l):
    for i in l:
        if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
            if i in 'abcABC':
                print (2,end='')
            elif i in 'defDEF':  
                print (3,end='')
            elif i in 'ghiGHI':
                print (4,end='')
            elif i in 'jklJKL':
                print (5,end='')
            elif i in 'mnoMNO':
                print (6,end='')
            elif i in 'pqrtPQRT':
                print (7,end='')
            elif i in 'tuvTUV':
                print (8,end='')
            else:
                print (9,end='')
        else:
            print (i,end='')
    print ('')    
l=str(input('>>>'))
getNumber(l)
'''
'''
#E6
def reverse(s):
    s= list(reversed(s))
    print ''.join(s)
s=list(raw_input('>>>'))
reverse(s)
'''
'''
#E7
def checkCard(card_num):
    card_list = list(card_num)
    Res = 0
    Res_2 = 0
    for i in range(len(card_list)):
        res = int(card_list[i]) * 2  
        if res >= 10:
            res_1 = res % 10
            res_2 = res // 10
            res_3 = res_2 + res_1
            Res += res_3
        else:
            Res += res

        if i % 2 !=0: 
            Res_2 += int(card_list[i])

    RES = Res + Res_2
    if RES % 10 == 0:
        print('yes')
    else:
        print('no')
card_num = '438857601840707'
checkCard(card_num)
'''
'''
#E8
def checkISBN(str_):
    str_list = list(str_)
    SUM = 0
    for i in range(len(str_list)):
        if i % 2 == 0:
            res = int(str_list[i]) * 3
        else:
            res = int(str_list[i])
        print (str_[i],end='')
        SUM +=res
    RES = 10 - SUM % 10
    if RES == 10:
        RES = 0
    print (RES)
str_ = input('>>')
checkISBN(str_)
'''

#E1


def a(*args):
    for i in args:
        best = 70
        if a>=best-10:
            print('Student '+str(i)+' score is '+str([a])+' and grade is A')
        elif a>=best-20:
            print('Student '+str(i)+' score is '+str([a]) +' and grade is B')
        elif a>=best-30:
            print('Student '+str(i)+' score is '+str([a]) +' and grade is C')
        elif a>=best-40:
            print('Student '+str(i)+' score is '+str(list(a)) +' and grade is D')
        else:
            print('Student '+str(i)+' sorce is '+str(list(a))+' and grage is F')


'''
#E2
list=[1,2,3,4,5,6,7,8,9]
list.reverse()
print list
'''
'''
#E3
def count(a):
    count=[]
    a = a.split()
    count=[]
    for i in range(0,101):
        count.append(0)
    for j in range (len(a)):
        count[int(a[j])]+=1
    for j in range (1,101):
        if count[j]!=0:
            if count[j]==1:
                print (str(j) + ' occurs ' + str(count[j])+' time ')
            else:
                print (str(j) + ' occurs ' + str(count[j])+ ' times ')
a=str(raw_input(">>>"))
count(a)
'''
'''
#E4
def average(a):
    SUM=0
    c=0
    d=0
    a=a.split()
    for i in range (len(a)):
        SUM=SUM+int(a[i])
    b=SUM/len(a)
    for i in range (len(a)):
        if int(a[i])>b:
            c+=1
        else:
            d+=1
    print ('average is '+str(b))
    print ('more than average have '+str(c))
    print ('less than average have '+str(d))
a=raw_input('>>>')
average(a)
'''

#E5
import random
def count(a):
    counts=[]
    for i in range (1000):
        a=random.randint(0,9)
        counts.append(a)
    print counts
a=random.randint(0,9)
count(a)
'''
#E6
'''
