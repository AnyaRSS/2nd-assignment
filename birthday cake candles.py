import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    # Write your code here
    tall = 0
    maximum = candles[0]
    for n in range(len(candles)):
        if candles[n] > maximum:
            maximum = candles[n]
    for el in candles:
        if el == maximum:
            tall = tall + 1
    return tall

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
