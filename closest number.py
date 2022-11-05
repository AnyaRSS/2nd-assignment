import math
import os
import random
import re
import sys

def closestNumbers(arr):
    # Write your code here
    for x in range(1, n):
        stored = arr[x]
        y = x - 1
        while y >= 0 and stored < arr[y]:
            arr[y+1] = arr[y]
            y = y-1
        arr[y+1] = stored
    """
    arr.sort()
    """
    t = []
    minimum = abs(arr[1] - arr[0])
    for i in range(1, n):
        d = abs(arr[i] - arr[i-1])
        if d == minimum:
            t.append(arr[i-1])
            t.append(arr[i])
        if d < minimum:
            minimum = d
            t = [arr[i-1], arr[i]]
    return t

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()