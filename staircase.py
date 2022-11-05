import math
import os
import random
import re
import sys

def staircase(n):
    # Write your code here
    for x in range(n):
        for y in range(n-x-1):
            print(' ', end="")
        for z in range(x+1):
            print('#', end="")
        print()

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
