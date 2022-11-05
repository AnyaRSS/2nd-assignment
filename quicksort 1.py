import math
import os
import random
import re
import sys

def quickSort(arr):
    # Write your code here
    p = arr[0]
    left = []
    right = []
    for x in range(n):
        if arr[x] < p:
            left.append(arr[x])
        elif arr[x] > p:
            right.append(arr[x])
    final = [*left, p, *right]
    return final

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
