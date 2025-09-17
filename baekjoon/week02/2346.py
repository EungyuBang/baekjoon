from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
value = list(map(int, input().split()))
move_num = deque([(i+1, value[i]) for i in range(N)])
ballon = []

while move_num :
  num, step = move_num.popleft()
  ballon.append(num)

  if move_num  :
    if step > 0 :
      move_num.rotate(-(step-1) if step > 0 else -step)
    
    

print(' '.join(map(str, ballon)))
# print(ballon)
