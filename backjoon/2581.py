import sys

M = int(sys.stdin.readline())

N = int(sys.stdin.readline())

primeNum_list = []


for i in range(M,N+1):
    if i==1:
        pass
    elif i==2:
        primeNum_list.append(i)
    else:
        for j in range(2, i):
            if i%j==0:
                break
            elif j==i-1:
                primeNum_list.append(i)


if primeNum_list:

    print(sum(primeNum_list))
    print(primeNum_list[0])

else:

    print("-1")
    



    

