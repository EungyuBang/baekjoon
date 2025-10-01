# 스티커 2n
# 2행 n열
# 스티커 떼면, 변을 공유하는 스티커 사용 못함 

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
  n = int(input())

  value = [list(map(int, input().split())) for _ in range(2)]

  if n == 1:  # 열이 하나뿐인 경우
    print(max(value[0][0], value[1][0]))
    continue

  dpTable = [[0] * n for _ in range(2)]

  dpTable[0][0] = value[0][0]
  dpTable[1][0] = value[1][0]
  dpTable[0][1] = dpTable[1][0] + value[0][1]
  dpTable[1][1] = dpTable[0][0] + value[1][1]

  for i in range(2, n) :
    dpTable[0][i] = max(dpTable[1][i-1], dpTable[1][i-2]) + value[0][i]
    dpTable[1][i] = max(dpTable[0][i-1], dpTable[0][i-2]) + value[1][i]
  
  print(max(dpTable[0][n-1], dpTable[1][n-1]))