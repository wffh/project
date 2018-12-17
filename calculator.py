#! /usr/bin/env python3
import sys

s = sys.argv[1:]

def calculate(y):
    r = y - 3500
    if r <= 0:
        sum = y - y*0.165
        return sum
    elif 0 < r <= 1500:
        sum = y - (y - y*0.165 - 3500)*0.03 - y*0.165 + 0
        return sum
    elif 1500 < r <= 4500:
        sum = y - (y - y*0.165 - 3500)*0.10 - y*0.165 + 105
        return sum
    elif 4500 < r <= 9000:
        sum = y - (y - y*0.165 - 3500)*0.20 - y*0.165 + 555
        return sum
    elif 9000 < r <= 35000:
        sum = y - (y - y*0.165 - 3500)*0.25 - y*0.165 + 1005
        return sum
    elif 35000 < r <= 55000:
        sum = y - (y - y*0.165 - 3500)*0.30 - y*0.165 + 2755
        return sum
    elif 55000 < r <= 80000:
        sum = y - (y - y*0.165 - 3500)*0.35 - y*0.165 + 5505
        return sum
    elif r > 80000:
        sum = y - (y - y*0.165 - 3500)*0.45 - y*0.165 + 13505
        return sum

for char in s:
    x, y = char.split(':')
    try:
        y = int(y)
    except:
        print("Parameter Error")
    print("{}:{:.2f}".format(x, calculate(y)))
