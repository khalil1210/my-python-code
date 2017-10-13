#https://www.hackerrank.com/challenges/magic-square-forming/problem
#!/bin/python3

import sys

def splitNumberToArray(a):
    b = [[a[0], a[1], a[2]], [a[3], a[4], a[5]], [a[6], a[7], a[8]]]
    return b

def costOfMakingMagic(a,b):
    sum = 0
    for x in range(0, 3):
        for y in range(0, 3):
            sum += abs(int(a[x][y])-int(b[x][y]))
    return sum

magicSquares = [ 276951438,
                 294753618,
                 438951276,
                 492357816,
                 618753294,
                 672159834,
                 816357492,
                 834159672 ]
s = []
for s_i in range(3):
   s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
   s.append(s_t)

minCost = 99999999999
for i in magicSquares:
    cost = costOfMakingMagic(s,splitNumberToArray(str(i)))
    #print(cost)
    if ( cost < minCost ):
        minCost = cost
print(minCost)






