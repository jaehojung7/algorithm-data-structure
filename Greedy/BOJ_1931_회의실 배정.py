# https://www.acmicpc.net/problem/1931

import sys
input = sys.stdin.readline
n = int(input())
timetable = [list(map(int, input().split())) for _ in range(n)]
# 회의 끝나는 시간을 기준으로 오름차순 정렬하기
timetable.sort(key=lambda timetable: (timetable[1], timetable[0]))
print(timetable)

end_time = 0
count = 0

# 다음 회의 시작시간 x가 이전 회의 끝나는 시간 y보다 늦으면: count +1 
for meeting in timetable:
     if meeting[0] > end_time:
         end_time = meeting[1]
         count += 1
print(count)