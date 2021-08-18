# https://www.acmicpc.net/problem/17608 막대기

import sys
input = sys.stdin.readline
n = int(input())

stack = [int(input().split('\n')[0]) for i in range(n)]

longest = 0

count = 0
for stick in stack[::-1]:
    if stick > longest:
        longest = stick
        count += 1

print(count)