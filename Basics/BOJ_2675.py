# https://www.acmicpc.net/problem/2675

import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    R, S = map(str, input().split())
    answer = ''
    
    for char in S:
        answer += char * int(R)
    print(answer)