# https://www.acmicpc.net/problem/9012 괄호

import sys
input = sys.stdin.readline

T = int(input())

input_list = [input().split('\n')[0] for string in range(T)]

for string in input_list:
    count_open = 0
    count_close = 0

    for char in string:
        if char == '(':
            count_open += 1
        elif char == ')':
            count_close += 1
            if count_close > count_open:
                break
        
    if count_close != count_open:
        print('NO')
    elif string.startswith('(') and string.endswith(')'):
        print("YES")