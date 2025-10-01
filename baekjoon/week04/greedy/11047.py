# greedy
# 동전 N개중 가치가 K 보다 큰건 우선제외
# K보다 가치가 작은 동전 중 가장 큰 동전 선택해서 K에서 뺴줌 -> 반복
# K = 0 될때까지 -> 빼줬던 수 cnt 
N, K = map(int, input().split())

value = []

for _ in range(N) :
  num = int(input())
  value.append(num)

value.reverse()

cnt = 0
for i in range(len(value)) :
  if value[i] > K :
    continue
  coin_count = K // value[i]
  cnt += coin_count
  K = K % value[i] # 업데이트

print(cnt)
