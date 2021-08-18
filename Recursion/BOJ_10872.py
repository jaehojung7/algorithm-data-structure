# https://www.acmicpc.net/problem/10872 팩토리얼

import sys
n = int(sys.stdin.readline())

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(n))