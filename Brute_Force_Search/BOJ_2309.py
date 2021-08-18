# https://www.acmicpc.net/problem/2309 일곱 난쟁이

import sys
from itertools import combinations

heights = []
for _ in range(9):
    heights.append(int(sys.stdin.readline()))

height_combinations = list(combinations(heights, 7))

for combination in height_combinations:
    if sum(combination) == 100:
        heights_sorted = sorted(combination)
        for height in heights_sorted:
            print(height)
        break