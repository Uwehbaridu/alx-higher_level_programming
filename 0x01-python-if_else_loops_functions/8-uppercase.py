#!/usr/bin/python3
def uppercase(s):
    for c in s:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            print(chr(ord(c) - 32), end="")
        else:
            print(c, end="")
            print()