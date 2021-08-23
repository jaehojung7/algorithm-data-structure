# https://www.acmicpc.net/problem/2751 수정렬2

import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    heapq.heappush(heap, int(input()))

for i in range(len(heap)):
    print(heapq.heappop(heap))
