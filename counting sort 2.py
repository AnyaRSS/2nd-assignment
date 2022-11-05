import math
import os
import random
import re
import sys

def countingSort(arr):
    # Write your code here
    count = [0] * (max(arr)+1)
    for num in arr:
        count[num] += 1
    sort = []
    for x in range(len(count)):
        while count[x] != 0:
            count[x] -= 1
            sort.append(x)
    return sort

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
