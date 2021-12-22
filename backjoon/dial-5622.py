dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

S = input()

T = 0

for i in S:

    for j in dial:

        if i in j:

            T += int(dial.index(j)) + 3

print(T)

