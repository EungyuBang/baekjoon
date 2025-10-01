N = int(input())

counsel = [list(map(int, input().split())) for _ in range(N)]

dpTable = [0] * (N + 1)

for i in range(N) :
  time = counsel[i][0]
  price = counsel[i][1]

  if i + time <= N :
    dpTable[i + time] = max(dpTable[i] + price, dpTable[i + time])
  
  dpTable[i+1] = max(dpTable[i+1], dpTable[i])

print(dpTable[N])   