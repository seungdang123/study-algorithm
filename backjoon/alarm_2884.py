h, m = input().split()

h = int(h)
m = int(m)

if m < 45 and h > 0:
    h = h-1
    m = (60 + m) - 45

elif m < 45 and h == 0:
    h = 23
    m = (60 + m) - 45

else:
    h = h
    m = m - 45


print(h, m)