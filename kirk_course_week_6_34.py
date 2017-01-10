#!/usr/bin/env python

def ipvalid(ip):
    ip=ip.split('.')
    try:
        if len(ip)!=4 or \
           all(int(octet)>255 for octet in ip) or \
           all(int(octet)<0 for octet in ip) or \
           int(ip[0])==127 or \
           int(ip[0])>223 or \
           (int(ip[0])==169 and int(ip[1])==254):
           return False
        else:
            return True
    except ValueError as val_err:
        return False


def ipdec2bin(ipdec):
    ip=ipdec.split('.')
    b_ip=[]
    for d_octet in ip:
        b_octet=bin(int(d_octet)).split('0b')[1].zfill(8)
        b_ip.append(b_octet)
    ipbin='.'.join(b_ip)
    return ipbin
