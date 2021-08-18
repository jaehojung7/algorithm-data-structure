# https://www.acmicpc.net/problem/10989 수정렬3

# 계수정렬을 사용하여 통과
import sys
n = int(sys.stdin.readline())
count = [0] * 10001

for _ in range(n):
    count[int(sys.stdin.readline())] += 1

for index in range(len(count)):
    if count[index] != 0:
        for _ in range(count[index]):
            print(index)


# 삽입 정렬 사용해보니 시간 초과
n = int(input())

array = []
array.append(input())

for _ in range(n - 1):
  array.append(input())

  for i in range(len(array) - 1, 0, -1):
    if array[i] == array[i - 1]:
      array.remove(array[i])
      break
    
    else:
      if len(array[i]) < len(array[i - 1]):
        array[i], array[i - 1] = array[i - 1], array[i]

      elif len(array[i]) > len(array[i - 1]):
        break

      else:
        array[i - 1], array[i] = sorted([array[i], array[i - 1]])
     
for string in array:
  print(string)