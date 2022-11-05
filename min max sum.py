import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    # Write your code here
    s = sum(arr)
    maximum = arr[0]
    minimum = arr[0]
    for n in range(len(arr)):
        if arr[n] > maximum:
            maximum = arr[n]
    for n in range(len(arr)):
        if arr[n] < minimum:
            minimum = arr[n]
    sum_min = s - maximum
    sum_max = s - minimum
    print(sum_min, sum_max)
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)