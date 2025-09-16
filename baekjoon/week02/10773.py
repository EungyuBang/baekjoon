import sys
input = sys.stdin.readline


K = int(input())
stack = []

for i in range(K) :
  nums = int(input())
  if nums != 0 :
    stack.append(nums)
  else :
    stack.pop()

print(sum(stack))

