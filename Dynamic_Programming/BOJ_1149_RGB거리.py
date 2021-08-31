# https://www.acmicpc.net/problem/1149

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().rstrip().split())) for i in range(n)]

# i에서 R을 선택한 경우: i-1의 G vs B 작은 값을 선택해서 더해준다
# i에서 G을 선택한 경우: i-1의 R vs B 작은 값을 선택해서 더해준다
# i에서 B을 선택한 경우: i-1의 R vs G 작은 값을 선택해서 더해준다

for i in range(1, 3):
    arr[i][0] += min(arr[i - 1][1], arr[i - 1][2])
    arr[i][1] += min(arr[i - 1][0], arr[i - 1][2])
    arr[i][2] += min(arr[i - 1][0], arr[i - 1][1])

# 누적된 최종값 중에서 가장 작은 값을 선택
print(min(arr[n - 1]))