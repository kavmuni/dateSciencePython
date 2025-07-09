import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
# site: https://www.hackerrank.com/challenges/dynamic-array/problem?isFullScreen=true
def dynamicArray(n, queries):
    # Write your code here
    last_answer = 0
    arr = [[0, 0],
           [0, 0]
          ]
    arr[0] = []
    arr[1] = []
    #print(len(queries))
    for rec in range(len(queries)):
        #print(queries)
        if queries[rec][0] == 1:
            idx = (queries[rec][1] ^ last_answer)
            arr[idx].append(queries[rec][2])
        elif queries[rec][0] == 2:
            print("queries[rec][1]: ", queries[rec][1])
            print("last_answer: ", last_answer)
            idx = (queries[rec][1] ^ last_answer)
            #arr[idx] = queries[rec][2]
            last_answer = (arr[idx][(queries[rec][2])])%2
            print(last_answer)
        print(arr[0])
        print(arr[1])
        print("************")


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    result = dynamicArray(n, queries)
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    # fptr.close()
