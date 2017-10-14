import sys

n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]

#removing duplicates
prevVal = scores[0]
scoresNoDuplicates = [prevVal]
for i in range(1,n):
    if prevVal != scores[i]:
        scoresNoDuplicates.append(scores[i])
        prevVal = scores[i]

for j in alice:
    aliceRank = 1
    for i in range(0,len(scoresNoDuplicates)):

        if j >= scoresNoDuplicates[i]:
            print(aliceRank)
            break
        else:
            aliceRank+=1
            if (i == len(scoresNoDuplicates)-1):
                print(aliceRank)



#40 30 20 10

