import math
import os
import random
import re
import sys

def alternatingCharacters(s):
    # Write your code here
    count = 0
    for x in range(1, len(s)):
        if s[x] == s[x-1]:
            count +=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()