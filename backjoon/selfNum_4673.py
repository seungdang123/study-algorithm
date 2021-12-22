def d(n):

    next = n                       # next = 33

    for value in list(str(n)):     # [3,3]

        next += int(value)         # 33 + 3 + 3 = 39
    
    return next


excep = []

for count in range(10001):          # count = 33

    excep.append(d(count))          # excep.append(39)   


excep.sort()

for count in range(1,10000):

    if count in excep:
        continue
    else:
        print(count)