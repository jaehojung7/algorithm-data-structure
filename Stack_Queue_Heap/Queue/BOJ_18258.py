# https://www.acmicpc.net/problem/18258 큐2

import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

input_array = [input().split('\n')[0] for i in range(n)]
queue = deque()

for string in input_array:
    # push X: 정수 X를 큐에 넣는 연산이다.
    if string.split()[0] == 'push':
        queue.append(string.split()[1])
    
    # pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif string == 'pop':
        if len(queue) != 0:
            print(queue[0])
            queue.popleft()
        else:
            print(-1)

    # size: 큐에 들어있는 정수의 개수를 출력한다.
    elif string == 'size':
        print(len(queue))
    
    # empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
    elif string == 'empty':
        if len(queue) != 0:
            print(0)
        else:
            print(1)
    # front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif string == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)

    # back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif string == 'back':
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)
