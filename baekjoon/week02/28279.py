import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
nums = deque([])

for _ in range(N) :
  num = input().split()

  if num[0] == '1' :
    nums.appendleft(int(num[1]))
  elif num[0] == '2' :
    nums.append(int(num[1]))
  elif num[0] == '3' :
    if nums :
      print(nums.popleft())
    else :
      print(-1)
  elif num[0] == '4' :
    if nums :
      print(nums.pop())
    else :
      print(-1)
  elif num[0] == '5' :
    print(len(nums))
  elif num[0] == '6' :
    if nums :
      print(0)
    else :
      print(1)
  elif num[0] == '7' :
    if nums :
      print(nums[0])
    else :
      print(-1)
  elif num[0] == '8' :
    if nums :
      print(nums[-1])
    else :
      print(-1)