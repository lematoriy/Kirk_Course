#!/usr/bin/env python

import paramiko
import time

# turn off paging in output
def disable_paging(remote_connection,command='terminal length 0\n',delay=1):
    remote_connection.send('\n')
    remote_connection.send(command)
    time.sleep(delay)
    output=remote_connection.recv(65535)
    return output

if __name__=='__main__':

    ip='192.168.100.1'
    username='misha'
    password='misha'

    # create connection object
    connection=paramiko.SSHClient()

    # ignore that ssh key is missing (only in test environment!!!)
    connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # establish connection
    connection.connect(ip,username=username,password=password)

    # invoke shell
    remote_connection=connection.invoke_shell()

    # set reading buffer
    #remote_connection.send('\n')
    #output=remote_connection.recv(65535)
    #print output

    # disable paging
    output=disable_paging(remote_connection)

    # send 'show version' command (\n in the end ="enter")
    remote_connection.send('\n')
    #remote_connection.send('show version\n')
    remote_connection.send('show ip int br\n')

    #wait for the command to complete
    time.sleep(1)

    output=remote_connection.recv(65535)
    print output

    connection.close()
