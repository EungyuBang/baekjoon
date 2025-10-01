import sys
input = sys.stdin.readline

N = int(input())

dpTable = [[0] * (N+1) for _ in range(9)]

for i in range(9) :
  for j in range(i) :
    N = int(input())