import math
import os
import random
import re
import sys

def bigSorting(unsorted):
    # Write your code here
    sort = []
    for x in sorted(unsorted, key=lambda x: int(x)):
        sort.append(x)
    return sort
    """
    unsorted = list(map(int, unsorted))
    for x in range(1, n):
        stored = unsorted[x]
        y = x - 1
        while y >= 0 and stored < unsorted[y]:
            unsorted[y+1] = unsorted[y]
            y = y-1
        unsorted[y+1] = stored
    unsorted = list(map(str,unsorted))
    return unsorted
    """

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
