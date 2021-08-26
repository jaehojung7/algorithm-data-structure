# https://www.acmicpc.net/problem/2178

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for i in range(n)]

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # (nx,ny)가 범위 안에 있고, 값이 1인 경우 최단 거리를 +1 하고 큐에 넣기
            if (0 <= nx < n) and (0 <= ny < m) and (graph[nx][ny] == 1):
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))       

    return graph[n - 1][m - 1]

print(bfs(0,0))



