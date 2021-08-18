# https://www.acmicpc.net/problem/10773 제로

import sys
input = sys.stdin.readline
n = int(input())

input_array = [int(input()) for i in range(n)]
stack = []

for i in input_array:
    if i == 0:
        stack.pop()
    else: 
        stack.append(i)
print(sum(stack))
