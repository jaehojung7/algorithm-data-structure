# https://www.acmicpc.net/problem/10819 차이를 최대로

import sys
from itertools import permutations

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

# n이 최대 8로 크지 않으므로 모든 순열 확인해보기
all_permutations = list(permutations(array, n))

largest_sum = 0
for permutation in all_permutations:
    result = 0
    for i in range(n - 1):
        result += abs(permutation[i] - permutation[i - 1])
    if result > largest_sum:
        largest_sum = result

print(largest_sum)
   