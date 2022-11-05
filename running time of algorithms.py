import math
import os
import random
import re
import sys

def runningTime(arr):
    # Write your code here
    shifts = 0
    for x in range(1, n):
        stored = arr[x]
        y = x - 1
        while y >= 0 and stored < arr[y]:
            arr[y+1] = arr[y]
            y = y-1
            shifts  += 1
        arr[y+1] = stored
    return shifts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
