import sys
input = sys.stdin.readline
from collections import deque


N,M = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []
for _ in range(N) :
  graph.append(list(map(int, input().strip())))


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue :
      x,y = queue.popleft()
      for i in range(4) :
        new_x = x + dx[i]
        new_y = y + dy[i]
        if new_x < 0 or new_y < 0 or new_x >= N or new_y >= M :
           continue       
        if graph[new_x][new_y] == 0 :
           continue        
        if graph[new_x][new_y] == 1 :
           graph[new_x][new_y] = graph[x][y] + 1
           queue.append((new_x, new_y))
           
    return graph[N-1][M-1]

print(bfs(0,0))