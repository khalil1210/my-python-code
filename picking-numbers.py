#https://www.hackerrank.com/challenges/picking-numbers/problem
#!/bin/python3

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
a.sort()

noOfOccurrences = []
for i in range(0,1000):
    noOfOccurrences.append(0)

for i in range(0,n):
    noOfOccurrences[a[i]]+=1

maxValue = 0
for i in range(0,len(noOfOccurrences)-1):
    tempSum = noOfOccurrences[i] + noOfOccurrences[i+1]
    if ( maxValue < tempSum ):
        maxValue = tempSum

print(maxValue)