import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]

def bfs_list(start) :
  visited = set()
  queue = deque([start])
  visited.add(start)

  while queue :
    node = queue.popleft()
    print(node, end=' ')

    for neighbor in graph[node] :
      if neighbor not in visited :
        queue.append(neighbor)
        visited.add(neighbor)
bfs_list(0)

V = len(graph)
def bfs_matrix(start) :
  visited = [False] * V
  queue = deque([start])
  visited[start] = True

  while queue :
    node = queue.popleft()
    print(node, end=' ')
    for i in range(V) :
      if graph[node][i] == 1 and not visited[i] :
        visited[i] = True
        queue.append(i)

bfs_matrix(0)