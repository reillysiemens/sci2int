#!/usr/bin/env python3

import sys

oldfile = open(str(sys.argv[1]), 'r', encoding='utf-8')
newfile = open(str(sys.argv[2]), 'w', encoding='utf-8')

for line in oldfile:
    sci_nums = line.lstrip(' ').rstrip('\n').split('  ')
    new_nums = list(map(lambda x: int(float(x)), sci_nums))
    print(' '.join(['{}'.format(d) for d in new_nums]), file=newfile)
