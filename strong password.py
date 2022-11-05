import math
import os
import random
import re
import sys

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    l = [0, 0, 0, 0]
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    for c in password:
        if c in numbers:
            l[0] = 1
        elif c in lower_case:
            l[1] = 1
        elif c in upper_case:
            l[2] = 1
        elif c in special_characters: 
            l[3] = 1
    count = sum(l)
    return max((6 - n), 4 - count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
