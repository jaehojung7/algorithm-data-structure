# https://www.acmicpc.net/problem/2294

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
input_array = set(int(input().split('\n')[0]) for _ in range(n))
visited = [0] * (k + 1)

queue = deque()
for num in input_array:
    if num > k:
        continue
    else:
        visited[num] = 1
        queue.append((num, 1))

print(queue)
print(visited)

while queue:
    sum, count = queue.popleft()
    if sum == k:
        print(count)
        break
    print()
    print(queue)
    print(visited)

    # 현재 sum과 각각의 num을 합해서 차례대로 큐에 넣어주기
    for num in input_array:
        if sum + num > k:
            continue
        # (sum + num)이 이전의 sum과 중복되지 않으면 visited에 체크 & count +1
        elif visited[sum + num] == 0: 
            visited[sum + num] = 1
            queue.append((sum + num, count + 1))

if sum != k:
    print(-1)


