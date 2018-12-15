#! /usr/bin/env python3
import sys

ls = sys.argv[1:]
emp = []

for new_ls in ls:
    if new_ls not in emp:
        emp.append(new_ls)

for x in emp:
    print(x, end=' ')
print()
