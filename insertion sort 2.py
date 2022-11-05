import math
import os
import random
import re
import sys

def insertionSort2(n, arr):
    # Write your code here
    for x in range(1, n):
        stored = arr[x]
        y = x - 1
        while y >= 0 and stored < arr[y]:
            arr[y+1] = arr[y]
            y = y-1
        arr[y+1] = stored
        print(*arr)
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
