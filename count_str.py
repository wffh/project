#! /usr/bin/env python3

def char_count(str):
    char_dct = set(str)
    for char in char_dct:
        print(char, str.count(char))

if __name__ == '__main__':

    s = input('Enter a string:')

    char_count(s)

