S = input()

alphabet = list(range(97,123))    #아스키코드 a ~ z 

for x in alphabet:

    print(S.find(chr(x)), end=" ")
