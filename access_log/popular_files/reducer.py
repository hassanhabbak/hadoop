#!/usr/bin/python

import sys

count = 0 # count of hits on link
oldKey = None
mostPopular = ("",0) # tuple to contain the most popular file

for line in sys.stdin:
    try: # to avoid erroneous data
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            # Something has gone wrong. Skip this line.
            continue

        thisKey, thisSale = data_mapped

        if oldKey and oldKey != thisKey:
            print oldKey, "\t", count
            if count > mostPopular[1]:
                mostPopular = (oldKey, count)
            oldKey = thisKey;
            count = 0

        oldKey = thisKey
        count += 1
    except:
       continue

if oldKey != None:
    print oldKey, "\t", count

print "MostPoular", "\t", mostPopular[0], "\t", mostPopular[1]

