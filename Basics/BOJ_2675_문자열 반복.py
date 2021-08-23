# https://www.acmicpc.net/problem/2675

import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    R, S = map(str, input().split())
    
    # 스트링S의 각각의 char을 R만큼 반복해서 answer 리스트에 넣어주기
    answer = [char * int(R) for char in S]
    
    print(''.join(answer))