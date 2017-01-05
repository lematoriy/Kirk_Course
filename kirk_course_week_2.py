
#!/usr/bin/env python

import re

# ip input - check if at least 3 octets are specified
while True:
    ip_address=raw_input("Enter the ip address: ")
    if len(ip_address.split("."))<3:
        print "Input Error: at least 3 octets should be specified"
    elif len(ip_address.split('.'))>4:
        print "Input Error: too many octets provided"
    else:
        break

# convert ip_address into list using . as separator
ip_add=ip_address.split(".")

# format list and append last octet if required
if len(ip_add)==3:
    ip_add.append('0')
else:
    ip_add[3]='0'
'''
alternatively:

ip_add=ip_add[:3]
ip_add.append('0')
'''

# build ip address back
network='.'.join(ip_add)

# convert first octet to binary and hex
first_octet_bin=bin(int(ip_add[0]))
first_octet_hex=hex(int(ip_add[0]))


# print resluts as a table with 20s column width
print '\n\n'
print "%20s %20s %20s" % ('NETWORK NUMBER','FIRST OCTET BINARY','FIRST OCTET HEX')
print "%20s %20s %20s" % (network, first_octet_bin,first_octet_hex)
print '\n\n'


entry1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
entry1.split()

print 'Entry line is: %s' % (entry1)
print 'ip prefix: %s' % (entry1.split()[1])
print 'AS Path: %s' % (entry1.split()[3:])
print '\n\n'

cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"

# using rex, .*?)\) - any number of characters before ) in non-greedy manner '?'
# - otherwise capture till last )
software=re.search('Software *\((.*?)\)',cisco_ios).group(1)
ios=re.search('Version *(.*),',cisco_ios).group(1)

print '\n\n'
print 'IOS details:'
print '%25s %25s' % ('Software','Version')
print '%25s %25s' % (software,ios)
print '\n\n'

print " END OF OPERATION "
print '\n\n'
