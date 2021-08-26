# https://www.acmicpc.net/problem/7569

import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().rstrip().split())
graph = [[list(map(int, input().rstrip().split())) for _ in range(n)] for _ in range(h)]

# 오른쪽, 왼쪽, 앞, 뒤, 위, 아래 방향 설정
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    queue = deque()
    min_day = 0

    # 익은 토마토를 큐에 넣어주기
    for k in range(h):
        for j in range(n):
            for i in range(m):
                if graph[k][j][i] == 1:
                    queue.append((i, j, k, min_day))
    
    
    while queue:
        # 현재 토마토의 위치를 큐에서 꺼내고 인접한 토마토들을 확인하기
        x, y, z, min_day = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            # 인접한 토마토의 위치가 상자 범위 안에 있고 아직 익지 않았다면 
            if (0 <= nx < m) and ( 0 <= ny < n) and (0 <= nz < h) and (graph[nz][ny][nx] == 0):
                # 그 토마토를 익게 하고 최소 일수를 1 더해서 큐에 추가
                graph[nz][ny][nx] = 1 
                queue.append((nx, ny, nz, min_day + 1))

    # 익지 않은 토마토가 하나라도 있다면 -1을 출력
    for k in range(h):
        for j in range(n):
            for i in range(m):
                if graph[k][j][i] == 0:
                    return -1
    
    return min_day # 토마토가 모두 익게 되는 최소 일수 출력

print(bfs())

