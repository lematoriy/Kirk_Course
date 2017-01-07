#!/usr/bin/env python

# import modules
import sys
import re
import pprint

# use command line for ip address input
try:
    ip=sys.argv[1].split('.')
except IndexError as e:
    print 'Error: One argument - IP address is expected. Try again.'
    sys.exit()

if len(sys.argv)>2:
    print 'Error: only one argument is expected. Try again.'
    sys.exit()

# ======================================================================
# ***  IV - ip validation
# task:
'''
IV. Create a script that checks the validity of an IP address.  The IP address should be supplied
on the command line.
    A. Check that the IP address contains 4 octets.
    B. The first octet must be between 1 - 223.
    C. The first octet cannot be 127.
    D. The IP address cannot be in the 169.254.X.X address space.
    E. The last three octets must range between 0 - 255.

    For output, print the IP and whether it is valid or not.
'''
# A - allow for 3 octet, append 0 if needed
if ip.count('')>0:
    print 'ERROR: Missing octet (. followed by empty space)'
    sys.exit()
elif len(ip)<3:
    print "ERROR: Input Error: at least 3 octets should be specified"
    sys.exit()
elif len(ip)>4:
    print "ERROR: Input Error: too many octets provided"
    sys.exit()
else:
    if len(ip)==3:
        ip.append('0')

# B - E
for octet in range(len(ip)):
    try:
        if int(ip[octet])<0 or int(ip[octet])>255:
            print "Invalid ip address value: octets should be in 0-255 range"
            sys.exit()
        if octet==0:
            if int(ip[octet])>223:
                print "Invalid ip address value: 1st octet shold be in 0-223 range"
                sys.exit()
            elif int(ip[octet])==127:
                print "Invalid ip address value: 1st octet cannot be 127"
                sys.exit()
            elif int(ip[octet])==169 and int(ip[1])==254:
                print "Invalid ip address value: ip cannot be in 169.254.x.x range"
                sys.exit()
    except ValueError:
        print 'Error: ip address should consist of integers separated with dots'
        sys.exit()
print "\nIp check status: valid"




#======================================================================
#  *** I -IP CONVERTER TO BINARY


#  CONVERT TO BINARY
b_ip=[]
for d_octet in ip:
    b_octet=bin(int(d_octet)).split('0b')[1].zfill(8)
    b_ip.append(b_octet)
ip_add='.'.join(ip)
bin_add='.'.join(b_ip)

print '\nPart I:\n'
print '%-15s | %-40s' % ("IP address",'Binary')
print '%-15s | %-40s' % (ip_add,bin_add)


#======================================================================
# ***  II - BGP path
entry1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24      157.130.10.233         0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"
print '\nPart II:\n'
print "%-20s | %-50s" % ("ip_prefix", "as_path")

# \s* - 0 or more whitespaces in greedy mode
# \S* - 0 or more non-whitespace characters in greedy mode
# \S.* - non-whitespace character followed by 0 or more characters
for entry in (entry1,entry2,entry3,entry4):
    bgp_rec=re.search('\*\s*(\S*)\s*(\S*)\s*(\S.*)',entry)
    print "%-20s | %-50s" % (bgp_rec.group(1),bgp_rec.group(3))

#======================================================================
# ***  III - show ip breif

show_ip_int_brief = '''
Interface       IP-Address  OK? Method  Status  Protocol
FastEthernet0   unassigned  YES unset   up      up
FastEthernet1   unassigned  YES unset   up      up
FastEthernet2   unassigned  YES unset   down    down
FastEthernet3   unassigned  YES unset   up      up
FastEthernet4   6.9.4.10    YES NVRAM   up      up
NVI0            6.9.4.10    YES unset   up      up
Tunnel1         16.25.253.2 YES NVRAM   up      down
Tunnel2         16.25.253.6 YES NVRAM   up      down
Vlan1           unassigned  YES NVRAM   down    down
Vlan10          10.220.88.1 YES NVRAM   up      up
Vlan20          192.168.0.1 YES NVRAM   down    down
Vlan100         10.220.84.1 YES NVRAM   up      up
'''
# process strig:
# remove leading and last line symbol '\n' and split by line
show_ip=show_ip_int_brief.strip('\n').splitlines()

'''
# - TAKE ONE
#covert each line in list of valuse separated by space
for line in range(len(show_ip)):
    show_ip[line]=show_ip[line].split()

# create list of records for interfaces in up/up state
show_ip_list=[]
for line in show_ip:
    if line[4]=='up' and line[5]=='up':
        record=(line[0],line[1],line[4],line[5])
        show_ip_list.append(record)

print '\nPart III:\n'
print "%-20s | %-20s | %-20s | %-20s" % ('INTERFACE_NAME','IP_ADDRESS','STATUS','PROTOCOL')
for record in show_ip_list:
    print "%-20s | %-20s | %-20s | %-20s" % (record[0],record[1],record[2],record[3])
'''
# - TAKE TWO
# create list of records for interfaces in up/up state
show_ip_list=[]
for record in show_ip:
    record_split=record.split()
    if len(record_split)==6:
            if_name, ip_addr, discard1, discard2, line_status, line_proto =record_split
            if line_status=='up' and line_proto=='up':
                show_ip_list.append((if_name,ip_addr,line_status,line_proto))
# - take one style is nicer
print '\nPart III:\n'
pprint.pprint(show_ip_list,indent=4, width=80,depth=None)
