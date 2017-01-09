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
look for _hostname>show cdp neighbors + spaces + $
         _hostname>show cdp neighbors details + spaces + $

if _hostname>show cdp neighbors:
    - look for "Device ID"
    - process following lines:
        re.search((\w+)\s+(.+)\s{2,}).group(1) - neighbor
        re.search((\w+)\s+(.+)\s{2,}).group(2) - interface
    - append neighbors[] with neighbor:interface
    - append cdp_dict[hostname] with neigbors:neighbors[]
'''



try:
    # opent cdp output file for reading
    cdp_file='/home/ubuntu/PYTHON/Exersise/Kirk_Course/kirk_course_week_5.txt'
    search_words={
                'cdp':'show cdp neighbors',
                'cdp_detail':'show cdp neighbors detail',
                'ip':'IP address: ',
                'model':'Platform:'
                }

    rex={
        'host_in_cdp':'(^\w+)>', #SW1>show cdp neighbors
        'host_in_cdp_detail':'Device ID: (\S+$)',
        'neighbors':'(^\S+)\s{2,}(\S.+?)\s{2,}', #R1                    Fas 0/11              153            R S I           881          Fas 1
        'ip_add':'IP address:\s*(\S*$)',
        'platform':'Platform:\s*?(.*?),.*'
        }

    cdp_output={}

    # store process nodes in cdp detail output
    processed=[]


    with open(cdp_file) as cdp_input:
        for line in cdp_input:
            line.strip('\n')

            #--- find and process the >show cdp neighobrs block
            if (search_words['cdp'] in line) and (search_words['cdp_detail'] not in line):
                hostname=re.search(rex['host_in_cdp'],line).group(1)
                if hostname not in cdp_output.keys():
                    cdp_output[hostname]={}
                cdp_output[hostname]['neighbors']={}
                #read until line contains 'Device ID'
                while 'Device ID' not in line:
                    line=cdp_input.next()
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
                            print 'hostname in cdp detail: %s' % (hostname)
                        if (hostname not in cdp_output.keys()) and (hostname not in processed):
                            cdp_output[hostname]={}
                        if search_words['ip'] in line:
                            cdp_output[hostname]['ip']=re.search(rex['ip_add'],line).group(1)

                        line=cdp_input.next().strip('\n')

                    except AttributeError as e:
                        print 'Error while parsing neighbors in line:\n'
                        print line
                        print 'Error message:\n'
                        print e
                        sys.exit()
                    #except StopIteration as e_iter:
                    #    print 'End of file'






except IOError as e:
    print "Error while opening cdp output file. Make sure the file exists\n"
    print "Error message:\n"
    print e


print 'Results:\n'
pprint.pprint(cdp_output)
