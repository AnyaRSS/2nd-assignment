import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    # Write your code here
    x = 0
    y = 0
    for n in range(len(a)):
        if a[n] > b[n]:
            x = x + 1
        elif a[n] < b[n]:
            y = y + 1
        else:
            continue
    return [x, y]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()