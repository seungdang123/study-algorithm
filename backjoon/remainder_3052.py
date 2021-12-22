arr = []

for i in range(10):

    n = int(input())
    arr.append(n % 42)


arr = set(arr)


print(len(arr))


'''

num_list = []
remainder_list = []
count = 0

for i in range(10):

    num = input()
    num_list.append(num)


for i in num_list:

    remainder = int(i)%42
    remainder_list.append(remainder)


for i in remainder_list:

    number = remainder_list.count(i)

    if number == 1:

        count  = count + 1

    else:

        count = count



print(count)

'''