#! /usr/bin/env python3
import sys

a = []
b = []
s = sys.argv[1:]

for x in range(0 ,len(s)):
    if len(s[x]) > 3:
        a.append(s[x])
    else:
        b.append(s[x])

for x in range(0, len(b)):
    print(b[x] , end=' ')

print()

for x in range(0, len(a)) :
    print(a[x], end=' ')

print()
