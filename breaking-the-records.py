#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    highest = scores[0]
    highest_game = 0
    lowest = scores[0]
    lowest_game = 0

    # print())
    for i in range(1, len(scores)):
        
        score = scores[i]

        if score > highest:
            highest = score
            highest_game+=1


        if score < lowest:
            lowest = score
            lowest_game+=1
            
    return [highest_game, lowest_game]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
