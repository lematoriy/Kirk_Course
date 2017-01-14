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
'''
'''
import re
txt='Internet Address 172.16.13.150/29, Area 303953, Attached via Network Statement'
rex=r'Internet Address (\S+?), Area (\d+?),'
x=re.match(rex,txt)
print x.group(1)
'''
import re
interfacenames=[
                'Loopback',
                'Ethernet',
                'FastEthernet',
                'GigabitEthernet',
                'Serial'
                ]
rex={
    'interface':re.compile(r'((' + r'|'.join(interfacenames) + r')\S+) is (up|down), line protocol is (up|down)'),
    'ip_area':re.compile(r'.*?Internet Address (\S+?), Area (\d+?),'),
    'process_area':re.compile(r'\s*?Process ID (\S+?),.*?Network Type (\S+?),'),
    'timers':re.compile(r'\s*?Timer intervals.*?, Hello (\d+?), Dead (\d+?),')
    }
line='  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5'
print re.match(rex['timers'],line).group(1)
