import sys
input = sys.stdin.readline
from collections import deque

cump_num = int(input())
connected_num = int(input())

node_list = [[] for _ in range(cump_num + 1)]

for _ in range(connected_num) :
  c1, c2 = map(int, input().split())
  node_list[c1].append(c2)
  node_list[c2].append(c1)


'''
bfs 풀이
def bfs(start) :
  visited= [False] * (cump_num + 1)
  queue = deque([start])
  visited[start] = True
  while queue :
    node = queue.popleft()
    for neighbor in node_list[node] :
      if not visited[neighbor] :
        visited[neighbor] = True
        queue.append(neighbor)
  return visited
visited = bfs(1)
count = visited.count(True) - 1
print(count)
'''

# dfs 풀이
visited = [False] * (cump_num + 1)

def dfs(node, visited) :
  visited[node] = True

  for neighbor in node_list[node]:
    if not visited[neighbor] :
      dfs(neighbor, visited)

dfs(1, visited)
count = visited.count(True) - 1
print(count)