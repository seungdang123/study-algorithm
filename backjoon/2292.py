
N = int(input())

start = 1
plus = 6
stair = 1

if N == 1:
    print(1)

else:

    while True:

        start += plus      
        stair += 1        

        if N <= start:    

            print(stair)
            break

        plus += 6         



