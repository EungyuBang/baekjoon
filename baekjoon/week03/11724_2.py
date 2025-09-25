import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M) :
  n1, n2 = map(int, input().split())
  graph[n1].append(n2)
  graph[n2].append(n1)

  
visited = [False] * (N + 1) #방문했는지 안 했는지 알아야하니까 False 선언

def bfs_linked(start) :
  queue = deque([start]) 
  visited[start] = True #처음 들어온 노드 트루로 바꿔줌

  while queue :
    node = queue.popleft()

    for neighbor in graph[node] :
      if not visited[neighbor] :
        visited[neighbor] = True
        queue.append(neighbor)
  
cnt = 0

for i in range(1, N+1) :
  if not visited[i] :
    bfs_linked(i)
    cnt += 1

print(cnt)