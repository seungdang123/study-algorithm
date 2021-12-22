# 숫자의 합

N = int(input())

a = list(map(int, input()))

sum = 0

for i in range(N):

    sum += a[i]


print(sum)
