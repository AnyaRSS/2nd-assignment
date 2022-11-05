import math
import os
import random
import re
import sys

def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    zero= 0
    for i in range(len(arr)):
        if arr[i] < 0:
            neg = neg + 1
        elif arr[i] > 0:
            pos = pos + 1
        else:
            zero = zero + 1
    ratio_pos = pos/len(arr)
    ratio_neg = neg/len(arr)
    ratio_zero = zero/len(arr)
    
    print(ratio_pos)
    print(ratio_neg)
    print(ratio_zero)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
