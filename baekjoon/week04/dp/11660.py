import sys
input = sys.stdin.readline

N , M = map(int, input().split())

numList = [list(map(int, input().split())) for _ in range(N)]

coord = [list(map(int, input().split())) for _ in range(M)]

dpTable = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
  for j in range(1, N+1):
    dpTable[i][j] = dpTable[i-1][j] + dpTable[i][j-1] - dpTable[i-1][j-1] + numList[i-1][j-1] # dpTable 에 더했을때의 모든 값 다 넣어놓음 

for x1, y1, x2, y2 in coord:
    result = dpTable[x2][y2] - dpTable[x1-1][y2] - dpTable[x2][y1-1] + dpTable[x1-1][y1-1]
    print(result)
