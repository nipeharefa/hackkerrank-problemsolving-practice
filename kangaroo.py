#!/bin/python3

# unsolved

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    a = x1
    b = x2

    jump = False
    
    count = 0
    while(a <= b):

        a+=v1
        if b < a:
            b+=v2

        # if (a < b and count == 1):
        #     jump = False
        #     break

        if a == b:
            jump = True
            break

        count+=1

    if jump:
        return 'YES'
    
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
