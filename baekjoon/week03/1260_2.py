import sys
input = sys.stdin.readline
from collections import deque


N, M, V = map(int, input().split())

node_list = [[] for _ in range(N + 1)]

for _ in range(M) :
  n1,n2 = map(int, input().split())
  node_list[n1].append(n2)
  node_list[n2].append(n1)

for i in range(len(node_list)) :
  node_list[i].sort()

dfs_order = []
bfs_order = []

visited = [False] * (N+1)
def dfs(start) :
  visited[start] = True
  dfs_order.append(start)
  for neighbor in node_list[start] :
    if not visited[neighbor] :
      dfs(neighbor)
dfs(V)

def bfs(start) :
  visited = [False] * (N+1)
  queue = deque([start])
  visited[start] = True

  while queue :
    node = queue.popleft()
    bfs_order.append(node)

    for neighbor in node_list[node] :
      if not visited[neighbor] :
        queue.append(neighbor)
        visited[neighbor] = True
bfs(V)

print(*dfs_order)
print(*bfs_order)