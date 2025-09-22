
# deque를 사용하여 BFS 구현에 활용
from collections import deque
# 빠른 입력을 위해 sys 모듈 사용
import sys
# input() 대신 sys.stdin.readline() 사용 (백준 등에서 빠른 입력 처리)
input = sys.stdin.readline
# 파이썬의 기본 재귀 제한(1000)을 100만으로 확장 (이 문제에서는 BFS만 사용하지만, 습관적으로 넣는 경우가 많음)
sys.setrecursionlimit(10 ** 6) # 너무 큰 값으로 제한을 늘리면 스택 메모리 초과로 프로그램이 터질 수 있음



# N: 정점 개수, M: 간선 개수, R: 시작 정점 번호
N, M, R = map(int, input().split())
# 각 정점별 인접 리스트 생성 (1번부터 N번까지)
node_list = [[] for _ in range(N+1)]


# 간선 정보 입력 받아 양방향 그래프 구성
for i in range(M) :
  u, v = map(int, input().split())
  node_list[u].append(v)
  node_list[v].append(u)


# 문제 조건: 방문 순서가 작은 정점부터 방문해야 하므로 오름차순 정렬
for i in range(1, N+1) :
  node_list[i].sort()


# 각 정점의 방문 순서를 저장할 리스트 (0번 인덱스는 사용하지 않음)
answer = [0] * (N+1)
# 방문 순서 카운터
cnt = 1


# BFS 함수: 시작 정점부터 너비 우선 탐색
def bfs(start) :
  global cnt
  visited = set() # 방문한 정점 집합
  queue = deque([start]) # 시작 정점을 큐에 넣음
  visited.add(start)

  while queue :
    node = queue.popleft() # 큐에서 정점 하나 꺼냄
    answer[node] = cnt # 방문 순서 기록
    cnt += 1
    # 인접한 정점들 중 방문하지 않은 정점 큐에 추가
    for neighbor in node_list[node] : 
      if neighbor not in visited :
        queue.append(neighbor)
        visited.add(neighbor)


# BFS 실행 (시작 정점 R)
bfs(R)
# 1번 정점부터 N번 정점까지 방문 순서 출력
print(*answer[1:], sep='\n')