import sys
input = sys.stdin.readline

T = int(input())
site = [list(map(int, input().split())) for _ in range(T)]

for n, m in site :
  dpTable = [[0]* (m+1)  for _ in range(n+1)]
  print(dpTable)