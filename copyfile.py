#! /usr/bin/env python3
i = 1
with open('/home/shiyanlou/shiyanlou.txt', 'r') as file:
    with open('/home/shiyanlou/shiyanlou_copy.txt', 'w') as object:
        for x in file.readlines():
            object.write(str(i) + ' ' + x)
            i += 1
