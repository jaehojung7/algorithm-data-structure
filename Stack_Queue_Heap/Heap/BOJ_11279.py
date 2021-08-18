# https://www.acmicpc.net/problem/11279 최대힙

# 우선순위 큐 힙 정렬
import sys
import heapq
input = sys.stdin.readline

def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, value)

    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

n = int(input())
input_arr = []

for i in range(n):
    input_arr.append(int(input()))

answer = heapsort(input_arr)

for i in range(n):
    print(answer[i])

