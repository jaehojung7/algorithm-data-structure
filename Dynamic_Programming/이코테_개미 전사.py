import sys
input = sys.stdin.readline

n = int(input())
input_array = list(map(int, input().split()))

# DP 테이블 초기화
dp = [0] * 100

dp[0] = input_array[0]
dp[1] = max(input_array[0], input_array[1])

# i번째 위치까지의 최대 식량은 (i-1)까지의 식량 vs (i-2)까지의 식량 + 현재 위치 (i) 식량
for i in range(2,n):
    dp[i] = max(dp[i - 1], dp[i - 2] + input_array[i])

print(dp[n - 1])
