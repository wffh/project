#! /usr/bin/env python3
import sys

s = sys.argv[1:]
ls = dict()
i = 1
for st in s:
    for x in st.split(':'):
        if i%2 != 0:
            ls[x] = 0
            t = x
        else:
            ls[t] = x
        i += 1
      #  ls[x[0]] = x[1]

for x,y in ls.items():
    print('ID:{} Name:{}'.format(x,y))

