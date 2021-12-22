# 거스름돈

# 거슬러 줘야 할 돈이 N원일 때 거술러 줘야 할 동전의 최소 개수 구하기.
# 카운터에는 500원, 100원, 50원, 10원짜리가 무한히 존재.

price = int(input("price: "))
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += price // coin
    price %= coin


print(count)