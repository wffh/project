#! /usr/bin/env python3
from sys import argv

for arg in argv[1:]:
    if len(arg) > 3:
        print(arg)
