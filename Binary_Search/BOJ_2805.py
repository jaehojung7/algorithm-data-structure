# https://www.acmicpc.net/problem/2805

import sys
input = sys.stdin.readline

def binary_search(array, num):
    start = 0
    end = max(array)

    answer = 0
    while start <= end:
        total = 0       
        mid = (start + end) // 2
        for i in array:
            if i > mid:
                total += i - mid
        if total < m:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    return answer

n, m = map(int, input().split())
input_array = list(map(int, input().split()))

print(binary_search(input_array, m))