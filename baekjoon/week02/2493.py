import sys
input = sys.stdin.readline
N = int(input())
heights = list(map(int, input().split()))

stack = []
ans = [0] * N

# for i in reversed(stack) :
for i in range(N) :
  while stack :
    if heights[i] < stack[-1][1] :
      ans[i] = stack[-1][0] + 1 
      break
    else :
      stack.pop()
  stack.append((i, heights[i]))

print(*ans)


   
