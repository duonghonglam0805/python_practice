#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
# def solve(s):
#     list = s.split(" ")
#     result = []
#     for i in range(len(list)):
#         if(list[i].isalpha()):
#             result.append(list[i].title())
#         else:
#             result.append(list[i])
#     return " ".join(result)

def solve(s):
    list = s.split(" ")
    result = []
    for i in range(len(list)):
        result.append(list[i].capitalize())
    return " ".join(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
