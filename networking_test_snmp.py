#!/usr/bin/env python

'''
R1#sh run | in snmp
snmp-server user mishav2c V2CALLRO v2c
snmp-server group V3ALLRO v3 priv read VIEWALLRO
snmp-server group V2CALLRO v2c read VIEWALL
snmp-server view VIEWALL ccitt included
snmp-server view VIEWALLRO iso.* included
snmp-server community mishacommunity RO
R1#
snmp-server user mishav3 V3ALLRO v3 auth sha mishamisha priv aes 128 mishamisha
'''
'''
ubuntu@ubuntu-VirtualBox:~$ snmpget -v 3 -u mishav3 -l authpriv -a SHA -A "mishamisha" -x AES -X "mishamisha" 192.168.100.1:161 .1.3.6.1.2.1.4.24.3.0
IP-FORWARD-MIB::ipCidrRouteNumber.0 = Gauge32: 2
ubuntu@ubuntu-VirtualBox:~$ snmpget -v 2c -c mishacommunity 192.168.100.1 system.sysUpTime.0
DISMAN-EVENT-MIB::sysUpTimeInstance = Timeticks: (664610) 1:50:46.10
'''

import pprint
from pysnmp.entity.rfc3413.oneliner import cmdgen

ip='192.168.100.1'
port=161
user2c='mishav2c'
comm='mishacommunity'
userv3='mishav3'
auth='mishamisha'
priv='mishamisha'

cmdGen = cmdgen.CommandGenerator()

#errorIndication, errorStatus, errorIndex, varBindNbrTable = cmdGen.nextCmd(cmdgen.CommunityData(comm),
#                                                                               cmdgen.UdpTransportTarget((ip, 161)),
#                                                                               '1.3.6.1.2.1.14.10.1.3')

#pprint.pprint(cmdGen.nextCmd(cmdgen.CommunityData(comm),cmdgen.UdpTransportTarget((ip, 161)),'1.3.6.1.2.1.1.3'))
#pprint.pprint(cmdGen.nextCmd(cmdgen.CommunityData(comm),cmdgen.UdpTransportTarget((ip, 161)),'1.3.6.1.2.1.4.21.1.1'))

errorIndication, errorStatus, errorIndex, varBindNbrTable = cmdGen.nextCmd(cmdgen.CommunityData(comm),
                                                                               cmdgen.UdpTransportTarget((ip, 161)),
                                                                               '1.3.6.1.2.1.1.3')

#pprint.pprint(errorIndication)
#pprint.pprint(errorStatus)
print '\n'
pprint.pprint(varBindNbrTable)
