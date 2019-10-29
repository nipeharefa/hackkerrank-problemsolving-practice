#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):

    if year == 1918:
        return '26.09.1918'

    date = 256 - 243

    # 1917 ke bawah kabisat hanya bisa di modulasi 4
    is_leap_year_under_1917 = (year <= 1917 and year % 4 == 0)

    # diatas 1918 aturan kabisat diubah
    is_leap_year = ((year > 1918) & (year%400 == 0 or ((year%4 == 0) & (year%100 != 0))))
    # if year <= 1917 and year > 1918:
    #     if is_leap_year or year <= 1800:
    #         date = 256 - 244

    if is_leap_year_under_1917 or is_leap_year:
        date = 256 - 244

    day_of_programmer = "%s.09.%d" % (date, year)

    return day_of_programmer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
