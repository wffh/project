#! /usr/bin/env python3

count = {}
def char_count(str):
    for char in str:
        c = count.get(char)
        if c is None:
            count[char] = 1
        else:
            count[char] += 1

    print(count)

if __name__ == '__main__':
    s = input('Enter a string')
    char_count(s)


