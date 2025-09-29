import sys
input = sys.stdin.readline

n = int(input())
numList = []

for _ in range(n) :
  nums = list(map(int, input().split()))
  numList.append(nums)

dpTable = []
for i in range(n) :
  dpTable.append([0] * (i + 1))

dpTable[0] = numList[0]

  #    [1][0] [1][1]
  #  [2][0] [2][1] [2][2]
  # [3][0] [3][1] [3][2] [3][3]
for i in range(1, n) : 
  for j in range(0, i+1) :
    if j == 0 :
      dpTable[i][j] = dpTable[i-1][j] + numList[i][j]
    elif j == i :
      dpTable[i][j] = dpTable[i-1][j-1] + numList[i][j]
    else :
      dpTable[i][j] = max(dpTable[i-1][j], dpTable[i-1][j-1]) + numList[i][j]

print(max(dpTable[n-1]))