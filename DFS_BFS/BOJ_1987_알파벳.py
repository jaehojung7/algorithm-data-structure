import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

r, c = map(int, input().split())
graph = [list(input().split('\n')[0]) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    queue = set()
    queue.add((0, 0, 1, graph[0][0]))
    
    answer = 0
    visited = []
    
    while queue:
        x, y, count, visited = queue.pop()
        answer = max(answer, count)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # (nx, ny)가 범위 안에 있고 중복되는 알파벳이 아닌 경우 count +1 & 큐에 추가
            if (0 <= nx < r) and (0 <= ny < c) and (graph[nx][ny]) not in visited:
                queue.add((nx, ny, count + 1, visited + graph[nx][ny]))
                
    return answer

print(bfs())