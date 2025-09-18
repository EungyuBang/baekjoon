from collections import deque
import sys
input = sys.stdin.readline

# test_case = int(input())
# for _ in range(test_case):
#   N, M = map(int, input().split())
#   value = list(map(int, input().split()))
#   num_list = deque((i, value[i]) for i in range(N))

#   while num_list :
#     for i in range(len(num_list)) :
#       if len(num_list) >= 2 :
#         if num_list[i][1] < num_list[i + 1][1] :
#           num_list.rotate(-1)
#         elif num_list[i][1] >= num_list[i + 1][1] :
#           if i == M :
#             print(i)
#             break
#           else : 
#             num_list.popleft()
#       else :
#         print(i)


test_case = int(input())
for _ in range(test_case):
  N, M = map(int, input().split())
  value = list(map(int, input().split()))
  num_list = deque((i, value[i]) for i in range(N))

  cnt = 0

  while num_list :
    left_doc = num_list.popleft()

    if any(left_doc[1] < i[1] for i in num_list) :
      num_list.append(left_doc) 
    else :
      cnt += 1
      if left_doc[0] == M :
        print(cnt)
        break
