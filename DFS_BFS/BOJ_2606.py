# https://www.acmicpc.net/problem/2606

import sys
input = sys.stdin.readline

def dfs(graph, v, visited):
    global count
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            count += 1
            dfs(graph, i, visited)
    return count

n = int(input()) # number_of_computers
m = int(input()) # number_of_networks

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * len(graph)
count = 0

print(dfs(graph, 1, visited))