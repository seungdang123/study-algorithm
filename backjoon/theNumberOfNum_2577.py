first = int(input())
second = int(input())
third = int(input())

result = first * second * third

list_result = list(str(result))

for i in range(10):
    print(list_result.count(str(i)))