a=10
b=20
c=a+b
def f1():
    print('f1 execution')
    a=11
    x=25
    def f2():
        print('f2 execution')
        b=22
        m=33
        print(b,m,a,x) 
    print(a,x,b,c)
    f2()
def f3():
    print('f3 execution')
    p=55
    q=66
    return p,q
f1()
f3()
print(a,b,c)
        
    

