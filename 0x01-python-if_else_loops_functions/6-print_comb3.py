#!/usr/bin/python3
for i in range(10):
    for j in range(i+1, 10):
        if i == 0 and j == 1:
            print("01", end="")
        else:
            print(", {:02d}{:2d}".format(i, j), end="")
            print("\n")
