# https://www.acmicpc.net/problem/2750 수정렬

import sys
n = int(sys.stdin.readline())

array = []
for _ in range(n):
  array.append(int(sys.stdin.readline()))

array.sort()

for i in range(n):
    print(array[i])