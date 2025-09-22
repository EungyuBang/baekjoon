import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

node_list = [[] for _ in range(N + 1)]
for _ in range(N - 1) :
  n1, n2 = map(int, input().split())
  node_list[n1].append(n2)
  node_list[n2].append(n1)

# 각 노드의 부모를 저장할 리스트를 만듭니다. 초기값은 0으로 설정합니다.
# 인덱스 1부터 N까지 사용합니다.
parent_node = [0] * (N + 1)
# 노드의 방문 여부를 체크할 리스트를 만듭니다.
# 초기값은 모두 False입니다.
visited = [False] * (N + 1)

# DFS(깊이 우선 탐색)를 수행하는 함수를 정의합니다.
def dfs(node) :
  # 현재 노드를 방문 처리합니다.
  visited[node] = True
  # 현재 노드와 연결된 모든 이웃 노드를 순회합니다.
  for neighbor in node_list[node] :
    # 만약 이웃 노드가 아직 방문되지 않았다면
    if not visited[neighbor] :
      # 이웃 노드의 부모를 현재 노드로 기록합니다.
      parent_node[neighbor] = node
      # 이웃 노드에 대해 DFS를 재귀적으로 호출합니다.
      dfs(neighbor)

dfs(1)

for i in range(2, N+1) :
  print(parent_node[i])

