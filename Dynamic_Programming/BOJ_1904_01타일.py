# https://www.acmicpc.net/problem/1904

import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

# ex) dp[3]은 dp[2]의 00, 11 뒤에 1을 붙여서 001, 111을 만들고
# dp[1]의 1 뒤에 1을 붙여서 11을 만들 수 있다. 
# 따라서 dp[i] = dp[i - 1] + dp[i - 2] -> 피보나치 수열 문제와 같은 방법이 적용된다
for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[n])
