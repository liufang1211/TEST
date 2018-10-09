class aa:
    def __init__(self):
        self.a=eval(raw_input('Enter a number:'))
    def fuc(self):
        if self.a%2==0:
            print('The number is a oushu')
        else :
            print('THe number is a jishu')
#    def fuc1(self):
if __name__=='__main__':
    aa().fuc()

