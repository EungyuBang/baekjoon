# 0으로 시작하면 안됨
# 1 연속 안됨
# 1, 10, 100, 101, 1000, 1001 가능
# 길이 N 
# 피보나치
import sys
input = sys.stdin.readline

N = int(input())

if N == 1 :
  print(1)
  exit()
elif N == 2 :
  print(1)
  exit()

dp = [0] * (N + 1)
dp[1] = 1
dp[2] = 1

for i in range(3, N+1) :
  dp[i] = (dp[i-1] + dp[i-2])

print(dp[N])