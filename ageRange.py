#! /usr/bin/env python3
# -*- coding:utf-8 -*-
from sys import argv

a = int(argv[1])
if 0 <= a < 10:
    print('you belong to kids')
elif 10 <= a < 18:
    print('you belong to teenager')
elif 18 <= a < 30:
    print('you belong to adult')
elif 30 <= a < 60:
    print('you belong to older')
elif 60 <= a < 123:
    print('you belong to oldest')
