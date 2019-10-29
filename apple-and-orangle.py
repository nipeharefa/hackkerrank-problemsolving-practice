#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # print("Solve my problem")
    apple_dalam_jarak = 0
    orange_dalam_jarak = 0

    for i in apples:
        c = i+a
        if c >= s and c <= t:
            apple_dalam_jarak+=1

    for i in oranges:
        c = i+b
        if c >= s and c <= t:
            orange_dalam_jarak+=1
    
    print(apple_dalam_jarak)
    print(orange_dalam_jarak)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
