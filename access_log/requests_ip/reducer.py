#!/usr/bin/python

import sys

count = 0 # count of hits on link
oldKey = None

for line in sys.stdin:
    try: # to avoid erroneous data
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            # Something has gone wrong. Skip this line.
            continue

        thisKey, thisSale = data_mapped

        if oldKey and oldKey != thisKey:
            print oldKey, "\t", count
            oldKey = thisKey;
            count = 0

        oldKey = thisKey
        count += 1
    except:
       continue

if oldKey != None:
    print oldKey, "\t", count

