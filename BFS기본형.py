from collections import deque

# 인접 리스트
graph_list = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}


def bfs_list(start) :
  visited = set()
  queue = deque([start])  
  visited.add(start)

  while queue :
    node = queue.popleft()
    print(node, end=' ')

    for neighbor in graph_list[node] :
      if neighbor not in visited :
        queue.append(neighbor)
        visited.add(neighbor)

bfs_list(0)
        
# 인접 행렬
graph_matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0]
]

V = len(graph_matrix)

def bfs_matrix(start):
    visited = [False] * V
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for i in range(V):
            if graph_matrix[node][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)

bfs_matrix(0)