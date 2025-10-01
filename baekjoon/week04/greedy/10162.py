import sys
input = sys.stdin.readline

T = int(input())

A = 300
B = 60
C = 10

cnt = [0] * 3

cnt[0] = T // A
cnt[1] = (T % A) // B
cnt[2] = (T % A % B) // C

if (T % A % B % C) == 0 :
  print(*cnt)
else :
  print(-1)