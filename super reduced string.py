import math
import os
import random
import re
import sys

def superReducedString(s):
    # Write your code here
    res = []
    for x in range(len(s)):
        if len(res) == 0 or res[-1] != s[x]:
            res.append(s[x])
        else:
            res.pop()
            
    if len(res) == 0:
        return 'Empty String'
    else:
        return "".join(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
