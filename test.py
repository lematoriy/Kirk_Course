import re
txt='Platform: Cisco 881, Capabilities: Router Switch IGMP'
rex=re.search('Platform:\s*?(.*?),.*',txt)
print rex.group(1)
