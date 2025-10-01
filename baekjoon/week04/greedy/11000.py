# 강의 끝나는 시간과 시작하는 시간이 크거나 같으면 그 강의는 강의실 하나만 이용
# 강의 끝나는 시간이 지금 하고 있는 강의보다 작으면 강의실 따로 하나 더 배정해야됨
# 시작하는 시간 기준으로 sort 해버리고 무조건 첫 강의 선택 ( 끝나는 시간이 더 낫나? ) -> 시작하는 시간 같으면 끝나는 시간도 보고 정렬
# 이후 timeTable [i][1] [i+1][0] 비교 [i][1]이 더큼 -> 끝 시간이 더 크니까 강의실 하나 더 배정 -> cnt += 1 
# [i+1][0] 이 더 큼 -> 시작 시간이 더 크니까 강의실 배정 필요 없음.
# 시작 시간과 끝나는 시간이 겹치는게 3개면... 첫번째꺼만 continue 하고 뒤에건 cnt += 1 해줘야됨
# 마지막에 print(cnt)
import sys
input = sys.stdin.readline
import heapq

N = int(input())

timeTable = []
for _ in range(N) :
  startTime, endTime = map(int, input().split())
  timeTable.append((startTime, endTime))
timeTable.sort()

heap = []
heapq.heappush(heap, timeTable[0][1])

for i in range(1, N) :
  start = timeTable[i][0]
  end = timeTable[i][1]
  if heap[0] <= start :
    heapq.heappop(heap)
  heapq.heappush(heap, end)

print(len(heap))