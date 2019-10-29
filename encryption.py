#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    row = math.floor(math.sqrt(len(s)))
    column = math.ceil(math.sqrt(len(s)))

    x = row * column

    if (x < len(s)):
        row+=1

    arr = []
    str = []

    for i in range(0, column):
        b = s[i*column:(i*column)+column]
        arr.append(b)

    # print(arr)
    r = []

    for i in range(0, row+1):
        c = ''
        for a in arr:
            if len(a) > i:
                c+=a[i]
        
        if c != '':
            r.append(c)

    return ' '.join([x for x in r])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
