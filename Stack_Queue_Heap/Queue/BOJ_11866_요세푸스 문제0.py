# https://www.acmicpc.net/problem/11866 요세푸스문제0

import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())

queue = deque([i for i in range(1, n + 1)])
answer = []
count = 0
while len(queue) > 0:
    count += 1
    if count % k != 0:
        queue.append(queue[0])
        queue.popleft()

    elif count % k == 0:
        answer.append(queue[0])
        queue.popleft()

print('<', end = '')
for i in range(len(answer)):
    if i != len(answer) - 1:
        print(answer[i], end = ', ')
    else:
        print(answer[i], end = '>')
