import sys
input = sys.stdin.readline
from collections import deque


N = int(input())
queue = deque(range(1, N+1)) # 이런식으로 큐안에 바로 데이터 넣기 가능


while len(queue) > 1 :
  queue.popleft()
  queue.append(queue.popleft()) # 맨 왼쪽 데이터 지우고 바로 추가 -> 왼쪽에서 제일 오른쪽으로 이동

print(queue[0])

