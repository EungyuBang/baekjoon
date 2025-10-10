# dp
# 그냥 피보나치 수열 점화식 만들면 됨
# 근데 N =1 -> 1, N-> 2 라서 따로 관리 해줄 필요 없을듯..? 아닌가?
# 어쨌든 점화식이 i = i-1 + i-2 라서 관리 해줘야할듯?
N = int(input())

if N == 1 :
  print(1)
  exit()
elif N == 2 :
  print(2)
  exit()

dp = [0] * (N + 1)
dp[1] = 1
dp[2] = 2

for i in range(3, N+1) :
  dp[i] = (dp[i-1] + dp[i-2]) % 15746


print(dp[N])