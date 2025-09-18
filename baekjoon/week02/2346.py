from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
value = list(map(int, input().split()))
move_num = deque([(i+1, value[i]) for i in range(N)]) # 풍선의 인덱스 , 풍선이 터졌을 때 이동해야 할 수 
ballon = []

while move_num :
  num, step = move_num.popleft()
  ballon.append(num)

  if move_num  :
      move_num.rotate(-(step-1) if step > 0 else -step)
    
    

print(' '.join(map(str, ballon)))
# print(ballon)



