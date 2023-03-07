#!/usr/bin/python3
or i in range(122, 96, -1):
    print("{0}{1}".format(chr(i), chr(i-32) if i % 2 == 0 else ""), end="")
