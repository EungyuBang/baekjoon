import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
K = int(input())

for i in range(K) :
  V, E = map(int, input().split())
  node_list = [[] for _ in range(V + 1)]
  for _ in range(E) :
    n1,n2 = map(int, input().split())
    node_list[n1].append(n2)
    node_list[n2].append(n1)

  color = [0] * (V+1)
  def dfs(start, c) :
    color[start] = c
    for neighbor in node_list[start] :
      if color[neighbor] == 0 :
        if not dfs(neighbor, -c) :
          return False
      elif color[neighbor] == c :
        return False
    return True
  
  TF = True

  for node in range(1, V+1) :
    if color[node] == 0 :
      if not dfs(node, 1) :
        TF = False
        break

  if TF :
    print('YES')
  else :
    print('NO')
