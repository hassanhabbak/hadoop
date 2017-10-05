#!/usr/bin/python

import sys

oldKey = None
highestSale = 0.0

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the highest sale amount

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", highestSale
        oldKey = thisKey;
        highestSale = 0.0

    oldKey = thisKey
    if float(thisSale) > highestSale:
        highestSale = float(thisSale)

if oldKey != None:
    print oldKey, "\t", highestSale

