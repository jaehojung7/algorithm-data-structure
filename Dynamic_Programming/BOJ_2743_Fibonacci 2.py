# https://www.acmicpc.net/problem/2748

import sys
input = sys.stdin.readline
n = int(input())

# Top-down method
dp = [0] * 101
def fb(num):
    if num == 1 or num == 2:
        return 1

    if dp[num] != 0:
        return dp[num]
    
    dp[num] = fb(num - 1) + fb(num - 2)
    return dp[num]

print(fb(n))


# Botton-up method
dp = [0] * 101
dp[1] = dp[2] = 1

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])