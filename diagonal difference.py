import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    # Write your code here
    diag1 = 0
    diag2 = 0
    for x in range(len(arr)):
        diag1 = diag1 + arr[x][x]
    for y in range(len(arr)):
        diag2 = diag2 + arr[y][len(arr)-y-1]
    return abs(diag1 - diag2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
