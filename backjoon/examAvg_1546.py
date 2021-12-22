import sys

n = int(sys.stdin.readline())

scores = list(map(int, sys.stdin.readline().split()))

highest = max(scores)

for i in range(n):

    scores[i] = scores[i]/highest*100





print(sum(scores)/n)