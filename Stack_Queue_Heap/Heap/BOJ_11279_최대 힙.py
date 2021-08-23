# https://www.acmicpc.net/problem/11279 최대힙

import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    if num == 0:
        # 힙이 비어 있지 않으면 최대값을 출력하고 힙에서 제거
        if heap:
            print(-(heapq.heappop(heap)))
        # 힙이 비어 있으면 0 출력
        else:
            print(0)
    else:
        # 자연수를 입력하면 힙에 추가
        heapq.heappush(heap, -num)