# https://www.acmicpc.net/problem/11725

import sys

# 재귀의 최대 깊이를 설정
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(graph, current, parents):

    # Check connected nodes
    for connected in graph[current]:
        if parents[connected] == 0:
            parents[connected] = current
            dfs(graph, connected, parents)

n = int(input())
graph = [[] for i in range(n + 1)]
for _ in range(n - 1):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

parents = [0] * (n + 1)

dfs(graph, 1, parents)

for i in parents[2:]:
    print(i)