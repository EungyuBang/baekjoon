# N 주어졌을 때 제곱수로 더할 수 있는 항의 최소개수
# 

import sys
input = sys.stdin.readline

N = int(input())

dpTable = [i for i in range(N+1)]

for i in range(1, N+1) :
  for j in range(1, int(i**0.5)+1) :
    square = j * j
    dpTable[i] = min(dpTable[i], dpTable[i-square] + 1)

print(dpTable[N])