import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

matrix = [list(map(int, input().strip())) for _ in range(N)]

V = len(matrix)

def bfs(start) :
  visited = [False] * V
  queue = deque([start])
  visited[start] = True

  while queue :
    node = queue.popleft()
    print(node)
    for i in range(V) :
      if matrix[node][i] == 1 and not visited[i] :
        visited[i] = True
        queue.append(i)
        