# https://www.acmicpc.net/problem/1181 단어정렬

import sys

N = int(sys.stdin.readline())
arr = []

for _ in range(51):
    arr.append([])

for num in range(N):
    str = sys.stdin.readline().split('\n')[0]
  
    
    if str not in arr[len(str)]:
        arr[len(str)].append(str)
        
for lst in arr:
    if len(lst) >= 1:
      lst.sort()
      for word in lst:
        print(word)