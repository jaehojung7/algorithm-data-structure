# https://www.acmicpc.net/problem/11047

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = sorted([int(input()) for i in range(n)], reverse = True)

count = 0
for coin in coins:
    if coin <= k:
        count += k // coin
        k %= coin

print(count)
