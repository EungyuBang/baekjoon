import sys
import heapq
input = sys.stdin.readline

left_heap = []
right_heap = []

N = int(input())

for _ in range(N) :
  nums = int(input()) 

  if not left_heap :
    heapq.heappush(left_heap, -nums)
    print(nums)
    continue

  mid_value = -left_heap[0]

  if nums < mid_value :
    heapq.heappush(left_heap, -nums)
  else :
    heapq.heappush(right_heap, nums)
  
  if len(left_heap) < len(right_heap) : # right_heap 이 더 많아지면 왼쪽으로 이동
    right_pop_num = heapq.heappop(right_heap)
    heapq.heappush(left_heap, -right_pop_num)

  if len(left_heap) > len(right_heap) + 1: # left_heap 이 1 더 많은 건 괜찮음 근데 2 이상 더 많으면 안됨
    left_pop_num = -heapq.heappop(left_heap)
    heapq.heappush(right_heap, left_pop_num)

  # if right_heap and -left_heap[0] > right_heap[0] : 
  #   left_val = -heapq.heappop(left_heap)
  #   right_val = heapq.heappop(right_heap) 
  #   heapq.heappush(left_heap, -right_val)
  #   heapq.heappush(right_heap, left_val)
  # 라이트 힙이 비어있지 않고 레프트힙의 루트값이(중간값) 이 오른쪽 루트보다 클때 스왑 
  # 백준에서 짝수일 때 왼쪽값 출력 조건 때문에 필요없음 조건 없으면 있어야함
  
  
  print(-left_heap[0])


