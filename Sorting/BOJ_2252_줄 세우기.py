# https://www.acmicpc.net/problem/2252
# queue를 활용하는 위상 정렬 문제  

import sys
from collections import deque
input = sys.stdin.readline


def topology_sort():
    answer = []
    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0: # 진입차수가 0인 노드를 큐에 넣기
            queue.append(i)

    while queue:
        current_node = queue.popleft()
        answer.append(current_node)
        
        # 현재 노드(current_node)가 queue에서 빠졌으므로 이 노드와 연결된 노드들의 진입차수를 1 빼주기
        for connected_node in graph[current_node]:
            indegree[connected_node] -= 1
            
            # 위의 결과로 진입차수가 0이 되는 노드들을 queue에 넣어주기
            if indegree[connected_node] == 0:
                queue.append(connected_node)

    for node in answer:
        print(node, end = ' ')

# n:노드의 개수, m: 간선의 개수
n, m = map(int, input().split())

# 모든 진입차수를 0으로 초기화
indegree = [0] * (n + 1)
 
# 그래프에 간선정보를 입력
graph = [[] for i in range(n + 1)]
for _ in range(m):
    A,B = map(int, input().split())
    graph[A].append(B) # 노드A에서 B로 이동 
    indegree[B] += 1 # B로 들어오는 진입 차수 1 증가

# print(graph)
# print(indegree)

topology_sort()