#! /usr/bin/env python3
import sys

ls = sys.argv[1:]
t = len(ls)
while t:
    for x in range(0, len(ls)):
        if ls.count(ls[x]) > 1:
            i = ls.count(ls[x])-1
            while i:
                ls.remove(ls[x])
                i -= 1
    t -= 1

for n in range(0, len(ls)):
    print(ls[n], end = ' ')
print()
