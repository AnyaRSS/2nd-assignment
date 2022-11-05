import math
import os
import random
import re
import sys

def hackerrankInString(s):
    # Write your code here
    final = 'hackerrank'
    count = 0
    for c in s:
        if c == final[count]:
            count += 1
            if count == len(final):
                return 'YES'
    return 'NO'
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
