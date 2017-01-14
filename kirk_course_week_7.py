#!/usr/bin/env python
'''
3.  In the following directory there is a file 'ospf_data.txt':

https://github.com/ktbyers/pynet/tree/master/learnpy_ecourse/class7/OSPF_DATA

This file contains the output from 'show ip ospf interface'.
Using functions and regular expressions parse this output to
display the following (note, I ended up using re.split() as
part of the solution to this problem):

Int:     Loopback0
IP:     10.90.3.38/32
Area: 30395
Type: LOOPBACK
Cost: 1

Int:     GigabitEthernet0/1
IP:      172.16.13.150/29
Area:  30395
Type:  BROADCAST
Cost:  1
Hello: 10
Dead: 40

'''
'''
ospf_infs={
            interfaceA:{
                        ip:
                        Process:
                        Area:
                        Type:
                        Cost:
                        Hello:
                        Dead:
                        }
            }
'''


import re
import pprint

def show_ospf_if(show_ospf_interface):
    ospf_infs={}
    interfacenames=[
                    'Loopback',
                    'Ethernet',
                    'FastEthernet',
                    'GigabitEthernet',
                    'Serial'
                    ]
    rex={
        'interface':re.compile(r'((' + r'|'.join(interfacenames) + r')\S+) is (up|down), line protocol is (up|down)'),
        'ip_area':re.compile(r'\s*?Internet Address (\S+?), Area (\d+?),'),
        'process_type_cost':re.compile(r'\s*?Process ID (\S+?),.*?Network Type (\S+?), Cost: (\d+?)'),
        'timers':re.compile(r'\s*?Timer intervals.*?, Hello (\d+?), Dead (\d+?),')
        }
    for line in show_ospf_interface:
        line=line.strip('\n')
        interface_new=re.match(rex['interface'],line)
        if  interface_new:
            interface=interface_new.group(1)
            state=interface_new.group(3) + '/' + interface_new.group(4)
            ospf_infs[interface]={}
            ospf_infs[interface]['State']=state
        elif re.match(rex['ip_area'],line):
            ospf_infs[interface]['IP']=re.match(rex['ip_area'],line).group(1)
            ospf_infs[interface]['Area']=re.match(rex['ip_area'],line).group(2)
        elif re.match(rex['process_type_cost'],line):
            ospf_infs[interface]['Process']=re.match(rex['process_type_cost'],line).group(1)
            ospf_infs[interface]['If_type']=re.match(rex['process_type_cost'],line).group(2)
            ospf_infs[interface]['Cost']=re.match(rex['process_type_cost'],line).group(3)
        elif re.match(rex['timers'],line):
            ospf_infs[interface]['Hello']=re.match(rex['timers'],line).group(1)
            ospf_infs[interface]['Dead']=re.match(rex['timers'],line).group(2)
    return ospf_infs

#-----------------------------------------------------------------------------------

ospf_file='/home/ubuntu/PYTHON/Exersise/Kirk_Course/kirk_course_week_7_ospf.txt'

with open(ospf_file) as ospf_file:
    show_ospf_interface=ospf_file.readlines()

ospf_if_data=show_ospf_if(show_ospf_interface)

pprint.pprint(ospf_if_data)
