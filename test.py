import re
uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
lookfor='week'
rex=r'.*?(\d*) '+ re.escape(lookfor) + r'.*'
print 'rex= ' + rex
x=re.search(rex,uptime1)
print x.group(0)
print x.group(1)
