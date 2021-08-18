# https://www.acmicpc.net/problem/1974 Z

def z(N, r, c):
    if N == 1:
        return 2*r + c
    else:
        if (r + 1) <= 2**(N-1):
            r_num = 0
        else:
            r_num = 1

        if (c + 1) <= 2**(N-1):
            c_num = 0
        else:
            c_num = 1

        return 2**(N-1) * 2**(N-1) * (2*r_num + c_num) + z(N-1, r % 2**(N-1), c % 2**(N-1))


N, r, c = map(int, input().split())
print(z(N, r, c))