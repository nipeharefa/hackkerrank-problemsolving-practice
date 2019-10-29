#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    # land = 0
    valley = 0
    step = 0

    for i in s[:n]:
        if i == 'U':
            step+=1

            if step == 0:
                valley+=1

        else:
            step-=1
            
    return valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
