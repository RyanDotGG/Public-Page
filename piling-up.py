# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/challenges/piling-up/problem
import sys
all_input = sys.stdin.read().split("\n")
for item in range(2,len(all_input),2):
    blocks = all_input[item].split(" ")
    stack = []
    result = "Yes"

    if int(blocks[0])>=int(blocks[-1]):
        stack.append(blocks[0])
        #del blocks[0]
    else:
        stack.append(blocks[-1])
        #del blocks[-1]

    while len(blocks) != 0:
        if int(blocks[0])>=int(blocks[-1]):
            if int(blocks[0])<=int(stack[-1]):
                stack.append(blocks[0])
                del blocks[0]
            else:
                result = "No"
                break

        elif int(blocks[-1])>=int(blocks[0]):
            if int(blocks[-1])<=int(stack[-1]):
                stack.append(blocks[-1])
                del blocks[-1]
            else:
                result = "No"
                break

        else:
            result = "No"
            break

    print(result)
