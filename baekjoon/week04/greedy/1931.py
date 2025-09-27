# N 개의 회의, 각 회의 I에 대해서 시작시간, 끝 시간 주어져있음
# 회의가 겹치기 않게 회의실 사용 -> 회의 시작시간 안 주어짐
# startTime, endTime 이렇게 받아와서 넣어버리면 됨
# 처음엔 가장 빨리 끝나는 회의를 선택 
# 
N = int(input())
 
timeTable = []

for _ in range(N) :
  startTime, endTime = map(int, input().split())
  timeTable.append((endTime, startTime))

timeTable.sort()


# 우선 첫번째는 무조건 선택 (이미 정렬 됐으니까)
# for 문 돌리면서 lastOutTime(이건 계속해서 초기화 해줘야됨) <= startTime 만족하는거 찾기 -> cnt += 1

lastOutTime = timeTable[0][0]
cnt = 1

for endT, startT in timeTable[1:] :
  if startT >= lastOutTime :
    cnt += 1
    lastOutTime = endT

print(cnt)