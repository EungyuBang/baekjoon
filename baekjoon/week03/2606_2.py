import sys
input = sys.stdin.readline
from collections import deque

cmp_num = int(input())
connect_num = int(input())

list = [[] for _ in range(cmp_num + 1)]

for _ in range(connect_num) :
  n1, n2 = map(int, input().split())
  list[n1].append(n2)
  list[n2].append(n1)

def bfs(start) :
  visited = [False] * (cmp_num + 1)
  queue = deque([start])
  visited[start] = True
  while queue :
    node = queue.popleft()
    for neighbor in list[node] :
      if not visited[neighbor] :
        visited[neighbor] = True
        queue.append(neighbor)
  return visited

visited = bfs(1)
count = visited.count(True) - 1 
print(count) 

