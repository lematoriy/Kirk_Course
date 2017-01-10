'''
foo=[]
def bar():
    foo.append('hi')
bar()
print foo

foo1=0
def bar1():
    foo1+=1
print bar1()

x=0
def bar(x):
    x+=1
    return x
bar(1)
print x
'''
'''
a='r1'
b='r2'
edge=(a,b)
print edge
'''
ip='10,1,1,1'
ip=ip.split('.')
print ip
