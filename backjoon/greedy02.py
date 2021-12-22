n, m = map(int, input().split(" "))

table = []
a = 0

for i in range(n):

    items = list(input().split(" "))

    table.append(items)


for i in range(1,len(table)):   # 1 ~ 2

    if min(table[i-1]) < min(table[i]):

        a = i


print(min(table[a]))

    