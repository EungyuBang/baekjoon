# 풀었다고 생각했지만 틀렸다고 나왔습니다...
import sys
input = sys.stdin.readline

N = int(input())

moveList = [list(map(int, input().split())) for _ in range(N)]

dpTable = [[0] * N for _ in range(N)]

dpTable[0][0] = 1

for i in range(N) :
  for j in range(N) :
    if dpTable[i][j] > 0 : # 이거 추가하니까 맞았음
      if i == N-1 and j == N-1 :  
        continue
      jumpRoute = moveList[i][j]
      if i + jumpRoute < N :
        dpTable[i+jumpRoute][j] += dpTable[i][j]    
      if j + jumpRoute < N :
        dpTable[i][j+jumpRoute] += dpTable[i][j]
print(dpTable[N-1][N-1])