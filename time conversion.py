import math
import os
import random
import re
import sys

def timeConversion(s):
    # Write your code here
    hour = s[:2]
    minute =s[3:5]
    second = s[6:8]
    AMorPM  = s[-2:]
    if AMorPM == 'PM':
        if hour == '12':
            hour ='12'
        else:
            hour = str(int(hour)+12)
    else:
        if hour == '12':
            hour = '00'
    return hour+':'+minute+':'+second

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()