# 인접 그래프
graph_list = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}

def dfs_list(node, visited = None) :
  if visited is None :
    visited = set()

  visited.add(node)
  print(node, end=' ')

  for neighbor in graph_list[node] :
    if neighbor not in visited :
      dfs_list(neighbor, visited)

dfs_list(0)


# 인접 행렬

graph_matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0]
]

V = len(graph_matrix)

def dfs_matrix(node, visited=None):
    if visited is None:
        visited = [False] * V
    visited[node] = True
    print(node, end=' ')
    for i in range(V):
        if graph_matrix[node][i] == 1 and not visited[i]:
            dfs_matrix(i, visited)

dfs_matrix(0)