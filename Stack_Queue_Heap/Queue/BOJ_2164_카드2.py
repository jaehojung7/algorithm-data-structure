# https://www.acmicpc.net/problem/2164 카드2

import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

queue = deque([i for i in range(1, n + 1)])

while len(queue) > 1:
    queue.popleft()
    queue.append(queue[0])
    queue.popleft()

print(int(queue[0]))
    


