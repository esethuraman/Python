#!/bin/python3

import sys

def minSteps(n, B):
    # Complete this function
    change_count = 0

    for i in range(len(B)-2):
        if (B[i:(i+3)]) =="010":
            # then the third position should be replaced with 1

            B = B[0:i+2] + B[i+2].replace("0", "1") + B[i+3:]
            change_count += 1
    # print(B)
    return change_count
n = int(input().strip())
B = input().strip()
result = minSteps(n, B)
print(result)
