import sys
from massielRatio import massielRatio

ratio = massielRatio(sys.stdin)

if ratio > 0.54 and ratio < 0.782:
    print 'Probably Massiel'
else:
    print 'Probably not Massiel'
