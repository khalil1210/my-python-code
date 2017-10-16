def findRankOfAliceRecursive(scores, start, end, val):
    midValue = int((start + end) / 2)
   # print("start", start, "end", end, "val", val, "mid_i", midValue, "midScore", scores[midValue])

    if val < scores[start]:
        return start
    elif scores[start] <= val < scores[midValue]:
        return findRankOfAliceRecursive(scores, start, midValue, val)
    elif scores[midValue] <= val < scores[midValue+1]:
        return midValue+1
    elif scores[midValue+1] <= val < scores[end]:
        return findRankOfAliceRecursive(scores, midValue+1, end, val)
    elif scores[end] <= val:
        return end+1
def findRankOfAlice(scores,aliceCurScore):
    # 1 2 4 5
    if ( len(scores) <= 1 ):
        if( scores[0] > aliceCurScore ):
            return 2
        else:
            return 1
    else:
        ans = findRankOfAliceRecursive(scores, 0, len(scores)-1, aliceCurScore)
        return ans

n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]

# removing duplicates
prevVal = scores[0]
scoresNoDuplicates = [prevVal]
for i in range(1, n):
    if prevVal != scores[i]:
        scoresNoDuplicates.append(scores[i])
        prevVal = scores[i]

scoresNoDuplicates.reverse()

length = len(scoresNoDuplicates)
for j in alice:

    answer = findRankOfAlice(scoresNoDuplicates,j)
    print(length - answer + 1)



# 40 30 20 10
