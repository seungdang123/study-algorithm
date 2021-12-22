n = int(input())    # 26

num = n

cnt = 0             # cycle 수 

while True:

    a = num // 10       # 2

    b = num % 10        # 6

    c = (a+b) % 10      # 8 % 10 = 8

    num = (b * 10) + c  # 60 + 8 = 68

    cnt = cnt + 1   #사이클 수 + 1

    if(num == n ):
        break;



print(cnt)