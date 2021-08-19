# https://www.acmicpc.net/problem/2751 수정렬2

import sys
import heapq
input = sys.stdin.readline

def heapsort(iterable):
    heap = []
    result = []

    for value in iterable:
        heapq.heappush(heap, value)

    for i in range(len(heap)):
        result.append(heapq.heappop(heap))
    return result

n = int(input())
input_arr = []

for i in range(n):
    input_arr.append(int(input()))

answer = heapsort(input_arr)
print(answer)

for i in range(n):
    print(answer[i])
