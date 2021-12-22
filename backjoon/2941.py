croatia = ["c=","c-","dz=","d-","lj","nj","s=","z="]


S = input()

for i in croatia:

    if i in S:

        S =  S.replace(f"{i}","#")

    

print(len(S))