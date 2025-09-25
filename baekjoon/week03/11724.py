from collections import deque
import sys
input = sys.stdin.readline

# 첫 줄에서 노드의 개수 N과 간선의 개수 M을 입력받음
N, M = map(int,input().split())

# N+1 크기의 리스트를 만들어 인접 리스트로 그래프를 표현
# 인덱스를 1부터 N까지 사용하기 위함
node_list = [[] for _ in range(N+1)]

# M개의 간선 정보를 입력받아 인접 리스트에 양방향으로 추가
for _ in range(M) :
  n1, n2 = map(int, input().split())
  # n1과 n2가 연결되어 있음을 표현
  node_list[n1].append(n2)
  # n2와 n1이 연결되어 있음을 표현
  node_list[n2].append(n1)

# N+1 크기의 visited 리스트를 만들어 노드의 방문 여부를 체크
# 초기값은 모두 False
visited = [False] * (N + 1)

# BFS(너비 우선 탐색)를 수행하는 함수 정의
def bfs(start) :
  # 큐(deque)에 시작 노드를 추가
  queue = deque([start])  
  # 시작 노드를 방문 처리
  visited[start] = True

  # 큐가 비어있지 않은 동안 반복
  while queue :
    # 큐의 맨 앞에서 노드를 꺼냄
    node = queue.popleft()
    # 현재 노드와 연결된 모든 이웃 노드를 순회
    for neighbor in node_list[node] :
      # 만약 이웃 노드가 아직 방문되지 않았다면
      if not visited[neighbor] :
        # 이웃 노드를 방문 처리
        visited[neighbor] = True
        # 이웃 노드를 큐에 추가하여 다음 탐색 대상으로 만듦
        queue.append(neighbor)

# 연결 요소의 개수를 세는 변수 초기화
cnt = 0

# 1번 노드부터 N번 노드까지 순서대로 반복
for i in range(1, N+1) :
  # 만약 현재 노드 i가 아직 방문되지 않았다면
  if not visited[i] :
    # 새로운 연결 요소가 시작된 것으로 판단하고 BFS 탐색 시작
    bfs(i)
    # BFS가 끝나면 하나의 연결 요소 탐색이 완료되었으므로 개수 1 증가
    cnt += 1

# 최종 연결 요소의 개수 출력
print(cnt)