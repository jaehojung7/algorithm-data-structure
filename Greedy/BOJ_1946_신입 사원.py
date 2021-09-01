# https://www.acmicpc.net/problem/1946

import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda arr: arr[0]) # 1차 성적 순위 순으로 정렬
    
    count = 1 # 1차 최고 성적은 이미 최종 선발에 포함
    max = arr[0][1] # 1차 최고 성적 지원자의 2차 성적을 max로 설정

    for i in range(1, n):
        if max > arr[i][1]:
            # i번 지원자의 2차 성적순위가 max보다 좋다면(낮은 숫자) count +1
            count += 1
            # i번 지원자의 2차 성적순위를 max로 설정
            max = arr[i][1]
    
    print(count)
