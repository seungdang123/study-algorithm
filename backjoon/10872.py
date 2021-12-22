# 팩토리얼 구하기
'''
import sys

N = int(sys.stdin.readline())

a = 1


for i in range(N, 1 , -1):

    a *= i

print(a)
'''

def f(n):
    if n==0:
        return 1
    return n*f(n-1)
    
print(f(int(input())))