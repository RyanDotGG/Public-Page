#!/bin/python3
#https://www.hackerrank.com/challenges/matrix-script/problem

import re

first_multiple_input = input().rstrip().split()
#print(first_multiple_input)
n = int(first_multiple_input[0])
#print(n)
m = int(first_multiple_input[1])
#print(m)
matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

#print(matrix)
string = ""
for i in range(m):
    for j in range(n):
        string += matrix[j][i]

output = re.sub(r"(\w)([^a-zA-Z0-9]+)(\w)", r"\1 \3", string)
print(output)
