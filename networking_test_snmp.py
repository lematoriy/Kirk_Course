#!/usr/bin/env python

'''
R1#sh run | in snmp
snmp-server user mishav2c V2CALLRO v2c
snmp-server group V3ALLRO v3 priv read VIEWALLRO
snmp-server group V2CALLRO v2c read VIEWALL
snmp-server view VIEWALL ccitt included
snmp-server community mishacommunity view VIEWALLRO RO
snmp-server user mishav3 V3ALLRO v3 auth sha mishamisha priv aes 128 mishamisha
R1#
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

#pprint.pprint(cmdGen.nextCmd(cmdgen.CommunityData(comm),cmdgen.UdpTransportTarget((ip, 161)),'1.3.6.1.2.1.14.10.1.3'))
#pprint.pprint(cmdGen.nextCmd(cmdgen.CommunityData(comm),cmdgen.UdpTransportTarget((ip, 161)),'1.3.6.1.2.1.4.21.1.1'))

errorIndication, errorStatus, errorIndex, varBindNbrTable = cmdGen.nextCmd(cmdgen.CommunityData(comm),
                                                                               cmdgen.UdpTransportTarget((ip, 161)),
                                                                               '1.3.6.1.2.1.1')

pprint.pprint(errorIndication)
pprint.pprint(errorStatus)
print '\n'
pprint.pprint(varBindNbrTable)
