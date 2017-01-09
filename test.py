import re
txt='Copyright (c) 1986-2010 by Cisco Systems, Inc.'
rex=re.search('.* by (.*)',txt)
print rex.group(1)
