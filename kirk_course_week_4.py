#!/usr/bin/env python

import sys
import re

# ======================================================================
# ***  I - ip input and validation
# task:
'''
I. Prompt a user to input an IP address.
Re-using some of the code from class3, exercise4--determine if the IP address is valid.
Continue prompting the user to re-input an IP address until a valid IP address is input.
'''
#------------------------------------------------------------------------
print '\n'
print '='*10 + '  PART I  ' + '='*10

entries=0
while True:
    #safety trigger - exit after 5 attempts
    if entries<5:
        entries+=1
    else:
        print 'Too many mistakes. Program will exit now.'
        sys.exit()
    ip_add=raw_input('\nPlease enter a valid ip address (4th octet set to .0 if not provided): ').split('.')
    # check if 3 or 4 octets provided, append zero if needed
    # if error found go straigt to next while ..
    if ip_add.count('')>0:
        print 'ERROR: Missing octet (. followed by empty space)'
        continue
    elif len(ip_add)<3:
        print "ERROR: Input Error: at least 3 octets should be specified"
        continue
    elif len(ip_add)>4:
        print "ERROR: Input Error: too many octets provided"
        continue
    else:
        if len(ip_add)==3:
            ip_add.append('0')
    # check ip address validity, if error found break out of for.. loop
    # with check flag set to 'not_valid'
    check=''
    for octet in range(len(ip_add)):
        try:
            if int(ip_add[octet])<0 or int(ip_add[octet])>255:
                print "Invalid ip address value: octets should be in 0-255 range"
                check='not_valid'
                break
            elif octet==0:
                if int(ip_add[octet])>223:
                    print "Invalid ip address value: 1st octet shold be in 0-223 range"
                    check='not_valid'
                    break
                elif int(ip_add[octet])==127:
                    print "Invalid ip address value: 1st octet cannot be 127"
                    check='not_valid'
                    break
                elif int(ip_add[octet])==169 and int(ip_add[1])==254:
                    print "Invalid ip address value: ip cannot be in 169.254.x.x range"
                    check='not_valid'
                    break
        except ValueError:
            print 'Error: ip address should consist of integers separated with dots'
            check='not_valid'
            continue
    # if check flag set to not_valid go to next while loop
    # else break out of while loop
    if check=='not_valid':
        continue
    else:
        print "\nIp check status: %s valid\n" % ('.'.join(ip_add))
        break


# ======================================================================
# ***  II - parse >show version
# task:

'''
II. Parse the below 'show version' data and obtain the following items (vendor, model, os_version,
uptime, and serial_number).  Try to make your string parsing generic i.e. it would work for other
Cisco IOS devices.

The following are reasonable strings to look for:

'Cisco IOS Software' for vendor and os_version
'bytes of memory' for model
'Processor board ID' for serial_number
' uptime is ' for uptime

Store these variables (vendor, model, os_version, uptime, and serial_number) in a dictionary.
Print the dictionary to standard output when done.

Note, "Cisco IOS Software...Version 15.0(1)M4...(fc1)" is one line.
'''
#-------------------------------------------------------------------------

show_version='''>>>>> show version data <<<<<
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support:
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
ROM: System Bootstrap, Version 12.4(22r)YB5, RELEASE SOFTWARE (fc1)

twb-sf-881 uptime is 7 weeks, 5 days, 19 hours, 23 minutes
System returned to ROM by reload at 15:33:36 PST Fri Feb 28 2014
System restarted at 15:34:09 PST Fri Feb 28 2014
System image file is "flash:c880data-universalk9-mz.150-1.M4.bin"
Last reload type: Normal Reload
Last reload reason: Reload Command

Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX1000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)

License Info:
License UDI:
-------------------------------------------------
Device#   PID                   SN
-------------------------------------------------
*0        CISCO881-SEC-K9       FTX1000038X

License Information for 'c880-data'
    License Level: advipservices   Type: Permanent
    Next reboot license Level: advipservices

Configuration register is 0x2102
>>>>> end <<<<<
'''
# build list of words to look for and target dictionary to store found values
# split the input by linesre.search(' *(\S*$)',line)
# process each line
# if line contains word of interest process it further at the same time capture keyword
# split line by whitespaces
# run through cases for each keyword and append dictionary

words_of_interest={
                    'ios_software':'Cisco IOS Software',
                    'model':'bytes of memory',
                    'cpu_id':'Processor board ID',
                    'uptime':' uptime is '
                    }

show_dict={
            'ios_software':'not found',
            'model':'not found',
            'cpu_id':'not found',
            'uptime':'not found'
            }

# show_dict={}

show_output=show_version.strip('\n').splitlines()

for line in show_output:
    for key,value in words_of_interest.iteritems():
        if value in line:
            if key=='ios_software':
                show_dict[key]=re.search('.*?\((.*?)\)',line).group(1)
            elif key=='model':
                show_dict[key]=re.search('^(.*?) processor',line).group(1)
            elif key=='cpu_id':
                show_dict[key]=re.search(' *(\S*$)',line).group(1)
            elif key=='uptime':
                show_dict[key]=re.search('uptime is (.*$)',line).group(1)
            else:
                print 'Something is wrong'

print '\n'
print '='*10 + '  PART II  ' + '='*10+ '\n'
for key,value in show_dict.iteritems():
    print '%20s | %s' % (key,value)



# ======================================================================
# ***  III - uptime converter
# task:
'''
III. Create a program that converts the following uptime strings to a time in seconds.

uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

For each of these strings store the uptime in a dictionary using the device name as the key.

During this conversion process, you will have to convert strings to integers.  For these string
to integer conversions use try/except to catch any string to integer conversion exceptions.

For example:
int('5') works fine
int('5 years') generates a ValueError exception.

Print the dictionary to standard output.
'''
#-------------------------------------------------------------------------

uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

uptime=(uptime1,uptime2,uptime3,uptime4)

uptime_dict={
            'year':0,
            'week':0,
            'day':0,
            'hour':0,
            'minute':0,
            'second':0
            }

uptime_seconds={}

try:
    for timeline in uptime:
        for key,value in uptime_dict.iteritems():
            uptime_dict[key]=0
            if key in timeline:
                rex=r'.*?(\d*) '+ re.escape(key) + r'.*'
                uptime_dict[key]=int(re.search(rex,timeline).group(1))

        time_in_seconds=uptime_dict['year']*365*24*60*60 + \
                        uptime_dict['week']*7*24*60*60 + \
                        uptime_dict['day']*24*60*60 + \
                        uptime_dict['hour']*60*60 + \
                        uptime_dict['minute']*60 + \
                        uptime_dict['second']

        uptime_seconds[timeline]=time_in_seconds

except ValueError as e:
    print 'Conversion to integer incurred error. Error message:\n'
    print e
    sys.exit()

print '\n'
print '='*10 + '  PART III  ' + '='*10 + '\n'
print '%20s | %s' % ('TIME IN SECONDS','RAW UPTIME STRING')
for key,value in uptime_seconds.iteritems():
    print '%20s | %s' % (value,key)
print '\n'
