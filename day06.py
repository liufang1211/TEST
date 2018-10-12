'''
for i in range (1,1001):
    a='http//:baidu.com/?page='
    b='?wd=aaa'
    url=a+str(i)+b
    print url
'''

'''
i=1
while i<=1000: 
    a='http//:baidu.com/?page='
    b='?wd=aaa'
    url=a+str(i)+b
    i+=1
    print url

'''
'''
A2=[1,2,1,2,1,2,1,3,6,4,3,4,6]
a2=[]
for i in A2:
    if i not in a2:
        a2.append(i)
print a2
'''

a4=[['a1',22,['360',100]],['a2',12,['baidu',4]],['a3',-1,['google',3]]]
'''
a4.sort(key=lambda x:x[2][1])
print a4
'''
a4=sorted(a4,key=lambda x:x[2][1])
print a4

