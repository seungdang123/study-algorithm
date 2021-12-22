N = int(input())

for i in range(N):
    
    a = input()                        # OOXXOXXOOO
    score = 0
    sumScore = 0

    for j in a:  

        if j == 'O':
            score += 1                 # O 일때 score 1 증가
        
        else:
            score = 0                  # X 일때 score 0 으로 초기화

        sumScore += score              # O이 연속되어 나올 경우 증가된 score 값을 sumScore에 더한다

    
    print(sumScore)