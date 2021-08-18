# https://www.acmicpc.net/problem/10828 스택

import sys
input = sys.stdin.readline
n = int(input())

input_array = [input().split('\n')[0] for i in range(n)]
stack = []

for string in input_array:
    # push X: 정수 X를 스택에 넣는 연산이다.
    if string.split()[0] == 'push':
        stack.append(string.split()[1])
    
    # pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif string == 'pop': 
        if len(stack) != 0:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)

    # size: 스택에 들어있는 정수의 개수를 출력한다.
    elif string == 'size': 
        print(len(stack))

    # empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
    elif string == 'empty':
        if len(stack) != 0:
            print(0)
        else:
            print(1) 
    
    # top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다
    elif string == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else: 
            print(-1)

