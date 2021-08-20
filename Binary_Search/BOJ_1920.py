# https://www.acmicpc.net/problem/1920

import sys
input = sys.stdin.readline

def binary_search(array, num):
    start = 0
    end = len(array) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == num:
            return 1
        elif array[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    return 0

n = int(input())
input_array = sorted(list(map(int, input().split())))

m = int(input())
target_array = list(map(int, input().split()))

for target in target_array:
    print(binary_search(input_array, target))
        