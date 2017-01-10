#!/usr/bin/env python

'''
2. Write a function that converts a list to a dictionary where the index of the
 list is used as the key to the new dictionary (the function should return the
 new dictionary).
'''
# with def() and for loop
def list2dict(_list):
    _dict={}
    i=0
    for item in _list:
        _dict[i]=item
        i+=1
    return _dict

_list=(1,2,3,4)
newdict=list2dict(_list)
print newdict

# with dict and zip
def list2dict2(inlist):
    outdict=dict(zip(range(len(inlist)),inlist))
    return outdict

inlist=('one','two','three','four')
newoutdict=list2dict2(inlist)
print newoutdict


#with enumerate
list3=('a','b','c')
dict3={}
for n,item in enumerate(list3):
    dict3[n]=item

print dict3

# with dict and enumerate
list4=('a','b','c')
dict4=dict(enumerate(list4))

print dict4

'''
3a.Convert the IP address validation code (Class4, exercise1) into a function,
take one variable 'ip_address' and return either True or False (depending on
whether 'ip_address' is a valid IP). Only include IP address checking in the
function--no prompting for input, no printing to standard output.
'''
print '\n Part 2' + '='*10

ip='a.1.1.1'

def ipvalid(ip):
    ip=ip.split('.')
    try:
        if len(ip)!=4 or \
           all(int(octet)>255 for octet in ip) or \
           all(int(octet)<0 for octet in ip) or \
           int(ip[0])==127 or \
           int(ip[0])>223 or \
           (int(ip[0])==169 and int(ip[1])==254):
           return False
        else:
            return True
    except ValueError as val_err:
        return False

if ipvalid(ip):
    print "Valid"
else:
    print "Not valid"



'''
3b. Import this IP address validation function into the Python interpreter shell
 and test it (use both 'import x' and 'from x import y').

>>> import kirk_course_week_6 as mymodule
>>> mymodule.ipvalid('10.1.1.1')
True
>>> mymodule.ipvalid('127.1.1.1')
False
>>> mymodule.ipvalid('169.254.1.1')
False
>>>
'''



'''
4. Create a function using your dotted decimal to binary conversion code from
Class3, exercise1. In the function--do not prompt for input and do not print
to standard output. The function should take one variable 'ip_address' and
should return the IP address in dotted binary format always padded to eight
binary digits (for example 00001010.01011000.00010001.00010111). You might want
to create other functions as well (for example, the zero-padding to eight binary
 digits).
'''

def ipdec2bin(ipdec):
    ip=ipdec.split('.')
    b_ip=[]
    for d_octet in ip:
        b_octet=bin(int(d_octet)).split('0b')[1].zfill(8)
        b_ip.append(b_octet)
    ipbin='.'.join(b_ip)
    return ipbin

print '\n Part 3' + '='*10
print ipdec2bin('192.168.2.1')



'''
5. Write a program that prompts a user for an IP address, then checks if the IP
address is valid, and then converts the IP address to binary (dotted decimal
format). Re-use the functions created in exercises 3 and 4 ('import' the
functions into your new program).
'''
