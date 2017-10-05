#!/usr/bin/python

import sys

salesTotal = 0
salesCount = 0
storeSalesCount = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale count
#
# It will also display total sales count and value at the end

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", storeSalesCount
        oldKey = thisKey;
        storeSalesCount = 0
	
    storeSalesCount += 1
    salesCount += 1
    oldKey = thisKey
    salesTotal += float(thisSale)

if oldKey != None:
    print oldKey, "\t", storeSalesCount
print "salesTotal", "\t", salesTotal
print "salesCountTotal", "\t", salesCount

