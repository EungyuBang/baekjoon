# dp
# 그냥 피보나치 수열 점화식 만들면 됨
# 근데 N =1 -> 1, N-> 2 라서 따로 관리 해줄 필요 없을듯..? 아닌가?
# 어쨌든 점화식이 i = i-1 + i-2 라서 관리 해줘야할듯?
import sys
input = sys.stdin.readline
n = int(input())

if n == 1 :
  print(1)
  exit()
elif n == 2 :
  print(2)
  exit()

dp = [0] * (n + 1)
dp[1] = 1
dp[2] = 2

for i in range(3, n+1) :
  dp[i] = (dp[i-1] + dp[i-2]) % 10007


print(dp[n])