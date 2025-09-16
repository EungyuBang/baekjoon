import sys
input = sys.stdin.readline

N = int(input())
sticks = [int(input()) for _ in range(N)]
heights = 0
cnt = 0

for h in reversed(sticks) :
  if h > heights :
    cnt += 1
    heights = h
  
print(cnt)