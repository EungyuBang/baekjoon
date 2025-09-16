import sys
input = sys.stdin.readline
# N - 나무수 , M - 가져가야 할 나무의 길이
N ,M = map(int, input().split())
heights = list(map(int, input().split()))
heights.sort()

left, right = 0, max(heights)
answer = 0

while left <= right :
  mid = (left + right) // 2
  cnt = 0
  for h in heights :
    if h > mid :
      cnt += h - mid

  if cnt >= M :
    anwser = mid
    up = mid + 1
  else :
    down = mid - 1


print(answer)