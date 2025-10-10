import sys
input = sys.stdin.readline

T = int(input())
site = [list(map(int, input().split())) for _ in range(T)]

for n, m in site :
  dpTable = [[0]* (m+1)  for _ in range(n+1)]

  for i in range(n+1) :
    for j in range(i, m+1) :
      if i == j :
        dpTable[i][j] = 1
      else :
        dpTable[i][j] = dpTable[i-1][j-1] + dpTable[i][j-1]

  print(dpTable[n][m])