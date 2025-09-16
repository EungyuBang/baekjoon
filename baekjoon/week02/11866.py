import sys
from collections import deque

input = sys.stdin.readline
killed_order = []

N, K = map(int,input().split())
queue = deque(range(1, N+1))

while queue :
  queue.rotate(-K + 1)
  killed_order.append(queue.popleft())


print("<" + ", ".join(map(str, killed_order)) + ">")
