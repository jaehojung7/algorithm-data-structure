import sys
input = sys.stdin.readline

numbers = input().split('-')
print(numbers)

answer = 0
for i in numbers[0].split('+'):
    answer += int(i)
    print(answer)

for j in numbers[1:]:
    for k in j.split('+'):
        answer -= int(k)
        # print(answer)


