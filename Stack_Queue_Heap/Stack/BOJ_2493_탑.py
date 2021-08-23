# https://www.acmicpc.net/problem/2493 탑

import sys
input = sys.stdin.readline

n = int(input())
input_arr = list(map(int, input().split()))
stack = []
answer = [0] * n

# 다시 볼 것
