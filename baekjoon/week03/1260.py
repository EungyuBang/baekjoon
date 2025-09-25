import sys
input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())

node_list = [[] for _ in range(N+1)]

dfs_order = []
bfs_order = []

for _ in range(M) :
  n1, n2 = map(int, input().split())
  node_list[n1].append(n2)
  node_list[n2].append(n1)

  for i in range(1, N + 1):
    node_list[i].sort()

for neighbor in node_list :
  neighbor.sort()

#dfs
def dfs(node, visited = None) :
  if visited is None :
    visited = set()
  visited.add(node)
  dfs_order.append(node)

  for neighbor in node_list[node] :
    if neighbor not in visited :
      dfs(neighbor,visited)
dfs(V)


#bfs
def bfs(start) :
  visited = set()
  queue = deque([start])
  visited.add(start)

  while queue :
    node = queue.popleft()
    bfs_order.append(node)
    for neighbor in node_list[node] :
      if neighbor not in visited :
        queue.append(neighbor)
        visited.add(neighbor)
bfs(V)

print(*dfs_order)
print(*bfs_order)