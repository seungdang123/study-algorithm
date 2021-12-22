import sys

T = int(sys.stdin.readline())


for i in range(T):

    H, W, N = map(int, sys.stdin.readline().split(" "))

    floor = N % H                 # 층 수 

    room = N // H + 1             # 방 호수 

    if floor == 0:                # N % H == 0 일 경우 꼭대기 층을 배정받으며, 호수는 N/H 가 된다.

        floor = H
        room = N//H




    print(floor * 100 + room)


