a, b, c = map(int, input().split(" "))

d = c-b

if d == -1 or d == 0:

    print(-1)


else:

    print(int((a/d)) + 1)
