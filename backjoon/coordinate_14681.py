a = int(input())
b = int(input())

if a == 0 or (-1000 > a and 1000 <a):
    a = int(input())
else:
    x = a
   
if b == 0 or (-1000 > b and 1000 <b):
    a = int(input())
else:
    y = b

if x > 0 and y > 0:
    print("1")

elif x < 0 and y > 0:
    print("2")

elif x < 0 and y < 0:
    print("3")

elif x > 0 and y < 0:
    print("4")