import math
import os
import random
import re
import sys

def camelcase(s):
    # Write your code here
    count = 1
    for el in s:
        if el.isupper():
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
