#!/usr/bin/env python

import re

# >>>>>>>>> Part I <<<<<<<<<<<<<<<<<<

class IPAddress(object):
    def __init__(self,ip_add_d):
        self.ip_add_d=ip_add_d
        self.ip_add_d_octets=ip_add_d.split('.')

    def display_in_binary(self):
        self.ip_add_b_octets=[]
        for octet in self.ip_add_d_octets:
            self.ip_add_b_octets.append(bin(int(octet)).split('0b')[1].zfill(8))
        print '.'.join(self.ip_add_b_octets)

    def display_in_hex(self):
        self.ip_add_h_octets=[]
        for octet in self.ip_add_d_octets:
            self.ip_add_h_octets.append(hex(int(octet)).split('0x')[1].zfill(4))
        print '.'.join(self.ip_add_h_octets)

    def is_valid(self):
        try:
            if len(self.ip_add_d_octets)!=4 or \
               all(int(octet)>255 for octet in self.ip_add_d_octets) or \
               all(int(octet)<0 for octet in self.ip_add_d_octets) or \
               int(self.ip_add_d_octets[0])==127 or \
               int(self.ip_add_d_octets[0])>223 or \
               (int(self.ip_add_d_octets[0])==169 and int(self.ip_add_d_octets[1])==254):
               return False
            else:
                return True
        except ValueError as val_err:
            return False



test_ip=IPAddress('192.168.100.1')
print test_ip.ip_add_d

test_ip.display_in_binary()
test_ip.display_in_hex()
print test_ip.is_valid()



# >>>>>>>>> Part II <<<<<<<<<<<<<<<<<<



class Uptime(object):

    def __init__(self,uptime):
        self.uptime=uptime

    def years(self):
        if 'years' in self.uptime:
            self.n_years=int(re.search(r'.*?(\d*) years.*',self.uptime).group(1))
        else:
            self.n_years=0
        #print self.years
        return self.n_years

    def weeks(self):
        if 'weeks' in self.uptime:
            self.n_weeks=int(re.search(r'.*?(\d*) weeks.*',self.uptime).group(1))
        else:
            self.n_weeks=0
        #print self.weeks
        return self.n_weeks

    def days(self):
        if 'days' in self.uptime:
            self.n_days=int(re.search(r'.*?(\d*) days.*',self.uptime).group(1))
        else:
            self.n_days=0
        #print self.days
        return self.n_days

    def hours(self):
        if 'hours' in self.uptime:
            self.n_hours=int(re.search(r'.*?(\d*) hours.*',self.uptime).group(1))
        else:
            self.n_hours=0
        #print self.days
        return self.n_hours

    def minutes(self):
        if 'minutes' in self.uptime:
            self.n_minutes=int(re.search(r'.*?(\d*) minutes.*',self.uptime).group(1))
        else:
            self.n_minutes=0
        #print self.minutes
        return self.n_minutes


    def uptime_seconds(self):
        if 'seconds' in self.uptime:
            self.n_seconds=int(re.search(r'.*?(\d*) seconds.*',self.uptime).group(1))
        else:
            self.n_seconds=0

        print 'years: %d' % self.years()
        print 'weeks: %d' % self.weeks()
        print 'days: %d' % self.days()
        print 'hours: %d' % self.hours()
        print 'minutes: %d' % self.minutes()
        print 'seconds: %d' % self.n_seconds


        self.uptime_seconds=int(self.n_seconds+ \
                            self.years()*365*24*60+ \
                            self.weeks()*7*24*60+ \
                            self.days()*24*60+ \
                            self.minutes()*60)
        #print self.uptime_seconds
        print 'total uptime in seconds: %d' % self.uptime_seconds
        return self.uptime_seconds


test_obj = Uptime('twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes')
test_obj.years()
test_obj.weeks()
test_obj.days()
test_obj.minutes()
x=test_obj.uptime_seconds()
print x

def test():
    uptime_strings = [
        'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes',
        '3750RJ uptime is 1 hour, 29 minutes',
        'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes',
        'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes',
        ]
    for uptime in uptime_strings:
        test_obj=Uptime(uptime)
        print '\nUptime output:' + test_obj.uptime
        #print 'Total uptime in seconds: '
        test_obj.uptime_seconds()

if __name__=='__main__':
    test()



# >>>>>>>>> Part III <<<<<<<<<<<<<<<<<<

class IPAddressWithNetmask(IPAddress):

    def __init__(self):
        (ip_add,net_mask)=IPAddress.split('/')
        IPAddress.__init__(self,ip_add)

    
