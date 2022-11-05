import math
import os
import random
import re
import sys


def insertionSort1(n, arr):
    # Write your code here
    stored = arr[-1]
    x = n - 1
    while x > 0 and stored < arr[x-1]:
        arr[x] = arr[x-1]
        print(*arr)
        x = x - 1
    arr[x] = stored
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)