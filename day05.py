'''
class aa:
    def __init__(self):
        self.a=eval(raw_input('Enter a number:'))
    def fuc(self):
        if self.a%2==0:
            print('The number is a oushu')
        else :
            print('THe number is a jishu')
    def fuc1(self):
        self.a=self.a ** 2
        print self.a
    def fuc2(self):
        self.a=self.a ** 3
        print self.a
if __name__=='__main__':
    #aa().fuc()
    AA=aa()
    AA.fuc1()
    AA.fuc2()
'''
'''
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def getArea(self):
        area = self.width * self.height
        print area
    def getPerimeter(self):
        perimeter = (self.width + self.height) * 2
        print perimeter
Rectangle(4,40).getArea()
Rectangle(4,40).getPerimeter()
'''



