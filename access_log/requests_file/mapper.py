#!/usr/bin/python

import sys
import re

# Regex to parse common log file line
p = re.compile(
    '([^ ]*) ([^ ]*) ([^ ]*) \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)'
    )

for line in sys.stdin:
    try: # to avoid erroneous data
        data = p.match(line).groups()
        if len(data) == 7:
            ip, identity, username, time, request, status, size = data
            print "{0}\t{1}".format(request, 1)
    except:
        continue

