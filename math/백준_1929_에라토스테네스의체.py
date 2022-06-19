# 백준 1929번 - 소수 구하기

# 시간 초과 에러
a, b = map(int, input().split())

answer = []

for i in range(a, b+1):
    temp = []
    
    for j in range(1, i+1):
        if i % j == 0:
            temp.append(j)
    
    
    if len(temp) == 2:
        answer.append(i)


for i in answer:
    print(i)
        

# 에라토스테네스의 체를 이용한 소수 구하기
n,m = map(int,input().split())

prime_list = [True]*(m+1)

print(prime_list)

prime_list[0] = False
prime_list[1] = False

for i in range(2,int(m**0.5)+1):
	if prime_list[i]:
		for j in range(i*2,m+1,i):
			prime_list[j] = False

for i in range(n,m+1):
	if prime_list[i]:
		print(i)