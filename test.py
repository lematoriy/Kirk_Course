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
import re
line='GigabitEthernet0/1 is up, line protocol is up'
interfacenames=[
                'Loopback',
                'Ethernet',
                'FastEthernet',
                'GigabitEthernet',
                'Serial'
                ]
#"r'((" + '|'.join(interfacenames) + ')\S+) is (up|down)' + "'"
#r'(' + '|'.join(interfacenames) + '\S+?) '
rex=r'((' + r'|'.join(interfacenames) + r')\S+) is (up|down)'
print rex
interface=re.match(rex,line)
print interface.group(1)
