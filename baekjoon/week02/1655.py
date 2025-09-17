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
  
  if len(left_heap) < len(right_heap) :
    right_pop_num = heapq.heappop(right_heap)
    heapq.heappush(left_heap, -right_pop_num)

  if len(left_heap) > len(right_heap) + 1:
    left_pop_num = -heapq.heappop(left_heap)
    heapq.heappush(right_heap, left_pop_num)


  if right_heap and -left_heap[0] > right_heap[0] :
    left_val = -heapq.heappop(left_heap)
    right_val = heapq.heappop(right_heap)
    heapq.heappush(left_heap, -right_val)
    heapq.heappush(right_heap, left_val)
  
  
  print(-left_heap[0])


