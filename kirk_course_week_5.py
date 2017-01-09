#!/usr/bin/env python

#import modules
import re
import sys
import pprint

# ======================================================================
# ***  I - parse cdp
# task:
'''
1. Parse the CDP data (see link above) to obtain the following information: hostname, ip,
model, vendor, and device_type (device_type will be either 'router', 'switch', or 'unknown').

From this data create a dictionary of all the network devices.

The network_devices dictionary should have the following format:

network_devices = {
     'SW1': { 'ip': '10.1.1.22', 'model': 'WS-C2950-24', 'vendor': 'cisco', 'device_type': 'switch' },
     'R1': { 'ip': '10.1.1.1', 'model': '881', 'vendor': 'Cisco', 'device_type': 'router' },
      ...
     'R5': { 'ip': '10.1.1.1', 'model': '881', 'vendor': 'Cisco', 'device_type': 'router' },
 }

Note, this data structure is a dictionary that contains additional dictionaries.  The key to the outer
dictionary is a hostname and the data corresponding to this key is another dictionary.  For example, for 'R1':

>>> network_devices['R1']
{'ip': '10.1.1.1', 'model': '881', 'vendor': 'Cisco', 'device_type': 'router'}

You can access a given attribute in the inner dictionary as follows:
>>> a_dict['R1']['ip']
'10.1.1.1'
'''
#_______________________________________________________________________________

'''
modified task:

cdp_dict={hostname1:{
                    'ip':ip,
                    'model':model,
                    'vendor':vendor,
                    'device_type':device_type,
                    'neighbors':{
                                 neighbor1:interface,
                                 neighbor2:interface
                                 ....
                                }
                    }
          hostname2:{
                    ...
                    }
          }

because of the structure:
for
    while
        next

at least one line between commands required


'''



try:
    # opent cdp output file for reading
    cdp_file='/home/ubuntu/PYTHON/Exersise/Kirk_Course/kirk_course_week_5.txt'
    search_words={
                'cdp':'show cdp neighbors',
                'cdp_detail':'show cdp neighbors detail',
                'ip':'IP address: ',
                'model':'Platform:',
                'vendor':'Copyright (c)'
                }

    rex={
        'host_in_cdp':'(^\w+)>', #SW1>show cdp neighbors
        'host_in_cdp_detail':'Device ID: (\S+$)',
        'neighbors':'(^\S+)\s{2,}(\S.+?)\s{2,}', #R1                    Fas 0/11              153            R S I           881          Fas 1
        'ip_add':'IP address:\s*(\S*$)',
        'model':'Platform:\s*?(\S.*?),.*?Capabilities: .*?(\S.*?) IGMP.*',
        'vendor':'.* by (.*)'
        }

    cdp_output={}

    # store process nodes in cdp detail output
    processed=[]


    with open(cdp_file) as cdp_input:
        for line in cdp_input:

            #--- find and process the >show cdp neighobrs block
            if (search_words['cdp'] in line) and (search_words['cdp_detail'] not in line):
                hostname=re.search(rex['host_in_cdp'],line).group(1)
                if hostname not in cdp_output.keys():
                    cdp_output[hostname]={}
                cdp_output[hostname]['neighbors']={}
                #read until line contains 'Device ID'
                while 'Device ID' not in line:
                    line=cdp_input.next().strip('\n')
                # skip header
                line=cdp_input.next().strip('\n')
                # read following lines unti empty line (strip off \n!) found or line contains '>'symbol
                while ('>' not in line) and (line!=''):
                    try:
                        neighbor=''
                        interfaces=''
                        neighbor=re.search(rex['neighbors'],line).group(1)
                        interface=re.search(rex['neighbors'],line).group(2)
                        cdp_output[hostname]['neighbors'][neighbor]=interface
                        #print 'neighbor: %s, interface: %s' % (neighbor,interface)
                        line=cdp_input.next().strip('\n')
                    except AttributeError as e:
                        print 'Error while parsing neighbors in line:\n'
                        print line
                        print 'Error message:\n'
                        print e
                        sys.exit()



            #--- find and process the >show cdp neighobrs detail block
            if search_words['cdp_detail'] in line:
                line=cdp_input.next().strip('\n')
                # process lines below until line with '>' is found or empty line
                while ('>' not in line) and (line!=''):
                    try:
                        #if device id found process lines below
                        if 'Device ID:' in line:
                            hostname=re.search(rex['host_in_cdp_detail'],line).group(1)
                            #print 'hostname in cdp detail: %s' % (hostname)
                        # if doesn't exist, create new dictionary for hostname
                        if (hostname not in cdp_output.keys()) and (hostname not in processed):
                            cdp_output[hostname]={}
                        # process keywords and update dictionary
                        if search_words['ip'] in line:
                            cdp_output[hostname]['ip']=re.search(rex['ip_add'],line).group(1)
                        elif search_words['model'] in line:
                            cdp_output[hostname]['model']=re.search(rex['model'],line).group(1)
                            cdp_output[hostname]['dev_type']=re.search(rex['model'],line).group(2)
                        elif search_words['vendor'] in line:
                            cdp_output[hostname]['vendor']=re.search(rex['vendor'],line).group(1)
                        # go to next line
                        line=cdp_input.next().strip('\n')

                    except AttributeError as e_attr:
                        print 'Error while parsing neighbors in line:\n'
                        print line
                        print 'Error message:\n'
                        print e_attr
                        sys.exit()
                    # there is a chance .next() would call eof
                    except StopIteration as e_iter:
                        break
                        print 'End of file'


except IOError as e:
    print "Error while opening cdp output file. Make sure the file exists\n"
    print "Error message:\n"
    print e

#print 'File opject:\n'
#print cdp_input
print 'Results:\n'
pprint.pprint(cdp_output)
