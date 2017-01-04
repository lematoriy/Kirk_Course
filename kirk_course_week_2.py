#!/usr/bin/env python

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
entry2 = "*  1.1.1.0/24      157.130.10.233         0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"
