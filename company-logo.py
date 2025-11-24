#!/bin/python3
#https://www.hackerrank.com/challenges/most-commons/problem
from collections import Counter


if __name__ == '__main__':
    s = "".join(sorted(input()))
    counter = Counter(s).most_common(3)
    for pair in counter:
        print(f"{pair[0]} {pair[1]}")
    
