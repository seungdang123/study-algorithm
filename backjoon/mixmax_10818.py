number = int(input())

number_list = list(map(int,input().split()))

max_num = number_list[0]

min_num = number_list[0]

for n in range(number):

    if number_list[n] > max_num:
        max_num = number_list[n]
    
    if number_list[n] < min_num:
        min_num = number_list[n]


print(min_num, max_num)