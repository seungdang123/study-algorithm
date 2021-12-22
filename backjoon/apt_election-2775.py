T = int(input())

for i in range(T):

    k = int(input())
    n = int(input())

    people = [i for i in range(1,n+1)]         # 0 층 사람들 인원 수 


    for x in range(k):

        for y in range(1, n):

            people[y] += people[y-1]           # 층 별 마다 인원 수

    print(people[-1])