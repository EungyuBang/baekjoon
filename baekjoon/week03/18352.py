import sys
input = sys.stdin.readline
from collections import deque

# X를 찍어 그러면 그 X에서 K거리만큼 떨어진 노드 출력

N, M, K, X = map(int, input().split())

list = [[] for _ in range(N+1)]

for _ in range(M) :
  A,B = map(int, input().split())
  list[A].append(B)

def bfs(start) :
  queue = deque([start])
  distance = [-1] * (N+1)
  distance[start] = 0

  while queue :
    node = queue.popleft()
    for neighbor in list[node] :
      if distance[neighbor] == -1 :
        distance[neighbor] = distance[node] + 1
        queue.append(neighbor)
  return distance

distance_K = bfs(X)

found = False

for i in range(1, N+1) :
  if distance_K[i] == K :
    print(i)
    found = True
  
if found == False :
  print(-1)