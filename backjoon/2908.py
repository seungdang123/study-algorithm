a, b  = map(list, input().split(" "))


a.reverse()
b.reverse()

x = ""
y = ""


for i in range(3):

    x += a[i]
    y += b[i]


if x>y:
    print(x)

else:
    print(y)