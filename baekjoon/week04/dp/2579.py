import sys
input = sys.stdin.readline

N = int(input())

numList = []
for _ in range(N) :
  num = int(input())
  numList.append(num)

dpTable = [0] * N
dpTable[0] = numList[0]

if N >= 2 :
  dpTable[1] = max(numList[0] + numList[1], numList[1])

if N >= 3 :
  dpTable[2] = max(numList[0] + numList[2], numList[1] + numList[2])

for i in range(3, N) :
  dpTable[i] = max(dpTable[i-3] + numList[i-1] + numList[i], dpTable[i-2] + numList[i])

print(dpTable[N-1])