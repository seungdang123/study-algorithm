n = int(input())
count = 1

while n > count:        # 해당 라인의 수열 갯수 확인 
    n -= count  
    count += 1  

if count % 2 == 0:                      #수열의 갯수가 짝수면 
    print(n, '/', count-n+1, sep='')
elif count % 2 == 1:                    #수열의 갯수가 홀수면
    print(count-n+1, '/', n, sep='')