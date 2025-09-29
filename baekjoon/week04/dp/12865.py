# 물품의수, 버틸 수 있는 무게
# 무게 , 가치

N, K = map(int, input().split())

weight = []
value = []

for _ in range(N) :
  w, v = map(int, input().split())
  weight.append(w)
  value.append(v)

dpTable = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if weight[i-1] <= j:  # 가방에 들어갈 수 있으면 
            dpTable[i][j] = max(dpTable[i-1][j], dpTable[i-1][j-weight[i-1]] + value[i-1])
        else:
            dpTable[i][j] = dpTable[i-1][j]  # 안 들어가면 이전 값 그대로

print(dpTable[N][K])