import sys
input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())

node_list = [[] for _ in range(N+1)]


for _ in range(M) :
  n1, n2 = map(int, input().split())
  node_list[n1].append(n2)
  node_list[n2].append(n1)

#dfs
def dfs(node, visited = None) :
  if visited is None :
    visited = set()
  
  visited.add(node)
  print(node, end=' ')

  for neighbor in node_list[node] :
    if neighbor not in visited :
      dfs(neighbor,visited)
print(V)

def bfs(start) :
  visited = set()
  queue = deque([start])
  visited.add(start)

  while queue :
    node = queue.popleft()
    print(node, end= ' ')

    for neighbor in node_list[node] :
      if neighbor not in visited :
        queue.append(neighbor)
        visited.add(neighbor)










#bfs