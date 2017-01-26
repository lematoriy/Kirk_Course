#!/usr/bin/env python

import telnetlib
import time

if __name__=='__main__':
    ip='192.168.100.1'
    username='misha'
    password='misha'

    TELNET_PORT=23
    TELNET_TIMEOUT=6
    READ_TIMEOUT=6

    remote_connection=telnetlib.Telnet(ip,TELNET_PORT,TELNET_TIMEOUT)
    #print dir(remote_connection)
    output=remote_connection.read_until('sername:',READ_TIMEOUT)
    remote_connection.write(username + '\n')

    output=remote_connection.read_until('ssword:',READ_TIMEOUT)
    #print output
    remote_connection.write(password + '\n')
    time.sleep(1)

    remote_connection.write('terminal length 0\n')
    time.sleep(1)
    output=remote_connection.read_very_eager()
    #print output
    remote_connection.write('\n')
    remote_connection.write('show version\n')
    time.sleep(1)
    output=remote_connection.read_very_eager()
    print output



    remote_connection.close()
