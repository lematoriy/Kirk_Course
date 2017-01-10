#!/usr/bin/env python

'''
5. Write a program that prompts a user for an IP address, then checks if the IP
address is valid, and then converts the IP address to binary (dotted decimal
format). Re-use the functions created in exercises 3 and 4 ('import' the
functions into your new program).
'''


import sys
sys.path.append('/home/ubuntu/PYTHON/Exersise/Kirk_Course')

from kirk_course_week_6_34 import ipvalid
from kirk_course_week_6_34 import ipdec2bin

while True:
    ip=raw_input('\nEenter IP address:\n')
    if ipvalid(ip):
        break
    else:
        print 'Invalid ip address - please try again.\n'

print ('%20s %s') % ('Decimal format: ',ip)
print ('%20s %s') % ('Binary format: ',ipdec2bin(ip))
