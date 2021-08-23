# https://www.acmicpc.net/problem/1260

import sys
input = sys.stdin.readline
from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    graph[v].sort()
    print(v, end = ' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        graph[v].sort()
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, input().split())
graph = [[] for i in range(n + 1)]
for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited_dfs = [0] * len(graph)
visited_bfs = [0] * len(graph)

dfs(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)
