import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6) # 파이썬 -> 재귀 호출 횟수 제한 (1000) , -> 재귀 깊이를 100만으로 확장 (너무 큰 값으로 제한을 늘리면 스택 메모리 초과로 프로그램이 터질 수 있음)


N, M, R = map(int, input().split())
node_list = [[] for _ in range(N+1)]

for _ in range(M) :
  u ,v = map(int, input().split())
  node_list[u].append(v)
  node_list[v].append(u)

for i in range(1, N+1) :
  node_list[i].sort(reverse=True)

answer = [0] * (N+1)
cnt = 1

def dfs (node, visited = None) :
  global cnt
  if visited is None :
    visited = set()
  
  visited.add(node)
  answer[node] = cnt
  cnt += 1

  for neighbor in node_list[node] :
    if neighbor not in visited :
      dfs(neighbor, visited)

dfs(R)
print(*answer[1:], sep='\n')





