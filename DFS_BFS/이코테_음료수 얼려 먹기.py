import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for i in range(n)]


def dfs(x,y):
    # 범위를 벗어나는 경우 False
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0: # 해당 좌표가 아직 0인 경우(방문하지 않은 상태)
        graph[x][y] = 1 # 그 좌표를 방문처리(1로 바꿔주기)하고 상하좌우 좌표도 체크
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    else:
        return False

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True: # 새로 방문한 지점인 경우 방문처리하고 count +1
            count += 1
print(count)
