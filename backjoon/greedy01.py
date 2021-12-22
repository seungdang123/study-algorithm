N, M, K = map(int, input().split(" "));

numbers = list(input().split(" "));

numbers.sort()

a = int(M//K)

b = int(M%K)




first = int(numbers[-1])

second = int(numbers[-2])



result = (first * a * K)  + (second * b)

print(result)
