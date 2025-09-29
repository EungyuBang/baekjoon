# 우선 첫 도시에서 다음 도시로 가는 기름만큼은 무조건 사야함
# 결국 중요한건 남은 도시의 금액이 지금 도시보다 비싸면 지금 도시에서 남은 거리만큼 다 사버려야함
# -> 남은 도시의 금액중 지금 도시보다 낮은 금액의 도시가 있는지 확인. (제일 낮은 기름 금액으로 갱신?) -> 있으면 그 도시까지의 거리만큼 지금 사버림
# -> 없으면 지금(제일싼) 남은 거리만큼 사버려야 함 

N = int(input())
roadValue = list(map(int, input().split())) # N-1
oilValue = list(map(int, input().split())) # N

minOilPrice = oilValue[0] # 이거 계속 업데이트 해야됨
totalCost = 0 # 이것도 업데이트 생각

for i in range(N-1) :
  totalCost += minOilPrice * roadValue[i]
  if oilValue[i+1] < minOilPrice :
    minOilPrice = oilValue[i+1]
    
print(totalCost)