N, C = map(int, input().split())
x = [int(input()) for _ in range(N)]
x.sort()
max_dis = 0

left , right = 1, x[-1] - x[0]

while left <= right :
  mid = (left + right) // 2
  cnt = 1
  last = x[0]

  for i in range(1, N) :
    if x[i] - last >= mid :
      cnt += 1
      last = x[i]

  if cnt >= C :
    max_dis = mid
    left = mid + 1
  else :
    right = mid - 1

    
print(max_dis)
