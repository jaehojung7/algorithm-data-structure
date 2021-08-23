# https://www.acmicpc.net/problem/1914 하노이탑

import sys
n = int(sys.stdin.readline())
count = 2 ** n - 1

def hanoi_tower(n, start, end):
  if n == 1:
    print(start, end)

  elif n > 1:
    # 시작과 목표지점이 아닌 임시지점
    temp = 6 - start - end
    #  n - 1 개의 원판을 임시지점으로 옮긴다
    hanoi_tower(n - 1, start, temp)
    #  시작지점에 남아 있는 1개의 원판을 목표지점으로 옮긴다
    print(start, end)
    #  n - 1개의 원판을 임시지점에서 목표지점으로 옮긴다
    hanoi_tower(n - 1, temp, end)
    
if n <= 20:
  print(count)
  hanoi_tower(n, 1, 3)

else:
  print(count)
