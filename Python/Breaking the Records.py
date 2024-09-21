#!/bin/python3

import os


def breakingRecords(scores):
    # Write your code here
    local_min = scores[0]
    local_max = scores[0]
    min_count = 0
    max_count = 0
    
    for score in scores:
        if score < local_min:
            local_min = score
            min_count += 1
        elif score > local_max:
            local_max = score
            max_count += 1
    
    return [max_count, min_count]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
