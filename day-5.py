'''
#E1
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        print width,height
    def getArea(self):
        area = self.width * self.height
        print area
    def getPerimeter(self):
        perimeter = 2 * (self.width + self.height)
        print perimeter
if __name__=='__main__':
    a=Rectangle(4,40)
    a.getArea()
    a.getPerimeter()
'''

'''
#E2
class Account:
    def  __init__(self,ID=0,balance=100,rate=0):
        self.__id=ID
        self.__balance=balance
        self.__annual_rate=rate
    def getMon_rate(self):
        mon_rate = self.__annual_rate/100/12.0
        return mon_rate
    def getMon(self):
        mon = self.__balance * self.__annual_rate/100/12.0
        return mon
    def withdraw(self,money):
        if money<self.__balance:
            print ('{}'.format(money))
        else:
            print('no money')
        self.__balance=self.__balance-money
        return self.__balance
    def depodit(self,money):
        self.__balance=self.__balance+money
        return self.__balance
    def amount(self):
        ph.getMon_rate()
        print self.__id
        money2 = self.__balance * (1+self.__balance/100/12.0)
        print money2
        
h=Account(1122,20000,4.5)
h.getMon_rate()
h.getMon()
h.withdraw(2500)
h.depodit(3000)

h.amount()
print(h.getMon_rate())
print(h.getMon())
'''
'''
#E3
import math
class RegularPolygon:
    def __init__(self,n=3,side=1,x=0,y=0):
        self.__n = n
        self.__side=side
        self.__x=x
        self.__y=y
    def getPerimeter(self):
        print self.__n * self.__side
    def getArea(self):
        area = (self.__n * (self.__side ** 2))/(4 * math.tan(math.pi/self.__n))
        print area
a=RegularPolygon()
a.getPerimeter()
a.getArea()
b=RegularPolygon(6,4)
b.getPerimeter()
b.getArea()
c=RegularPolygon(10,4,5.6,7.8)
c.getPerimeter()
c.getArea()
'''

'''
#E4
class Fan:
    def __init__(self,speed=1,on=False,radius=5,color='blue'):
        self.__speed=speed
        self.__on=on
        self.__radius=radius
        self.__color=color
    def a(self):
        print self.__speed,self.__on,self.__radius,self.__color
h=Fan(3,True,10,'yellow')
l=Fan(2,False,5,'blue')
h.a()
l.a()

'''

'''
#E5
class LinearEquation:
    def __init__(self,a,b,c,d,e,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f
        if self.__a*self.__d-self.__b*self.__c==0:
            print('no')
            exit(0)   #wu bao cuo jie shu dang qian dai ma
    def get(self):
        print self.__a,self.__b,self.__c,self.__d,self.__e,self.__f
    def isSolvable(self):
        print ('[+] True')
    def getX(self):
        x=(self.__e*self.__d-self.__b*self.__f)/(self.__a*self.__d-self.__b*self.__c)
        print x
    def getY(self):
        y=(self.__a*self.__f-self.__e*self.__c)/(self.__a*self.__d-self.__b*self.__c)
        print y
a,b,c,d,e,f=eval(raw_input("Enter a,b,c,d,e,f:"))
LinearEquation(a,b,c,d,e,f).get()
LinearEquation(a,b,c,d,e,f).isSolvable()
LinearEquation(a,b,c,d,e,f).getX()
LinearEquation(a,b,c,d,e,f).getY()

'''
#E6
class LinearEquation:
    def __init__(self,x1,y1,x2,y2x3,y3,x4,y4):
        self.__x1=x1
        self.__y1=y1
        self.__x2=y2
        self.__y2=y2
    def result(self):
        k1=(x1-x2)/(y1-y2)
        k2=(x3-x4)/(y3-y4)
        if k1==k2:
            print('no')
        else:
            x=
    def get(self):
        print self.__x1,self.__x2,self.__y1,self.__y2
    def isSolvable(self):
        m=self.__a * self.__d-self.__b * self.__c
        if m!=0:
            print 'True'
        elif m==0:
            print 'False'
    def getX(self):     
