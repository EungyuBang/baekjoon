
# sys 모듈을 사용하여 빠른 입력 처리 및 재귀 제한 설정
import sys
# input() 대신 sys.stdin.readline() 사용 (백준 등에서 빠른 입력 처리)
input = sys.stdin.readline
# 파이썬의 기본 재귀 호출 제한(1000)을 100만으로 늘림
# 깊은 재귀 호출이 필요한 DFS 등에서 호출 제한에 걸리지 않도록 설정
# 단, 너무 큰 값으로 설정하면 스택 메모리 초과로 프로그램이 강제 종료될 수 있으니 주의!
sys.setrecursionlimit(10 ** 6)



# N: 정점 개수, M: 간선 개수, R: 시작 정점 번호
N, M, R = map(int, input().split())
# 각 정점별 인접 리스트 생성 (1번부터 N번까지)
node_list = [[] for _ in range(N+1)]


# 간선 정보 입력 받아 양방향 그래프 구성
for _ in range(M) :
  u ,v = map(int, input().split())
  node_list[u].append(v)
  node_list[v].append(u)


# 문제 조건: 방문 순서가 작은 정점부터 방문해야 하므로 오름차순 정렬
for i in range(1, N+1) :
  node_list[i].sort()


# 각 정점의 방문 순서를 저장할 리스트 (0번 인덱스는 사용하지 않음)
answer = [0] * (N+1)
# 방문 순서 카운터
cnt = 1


# DFS 함수: 시작 정점부터 깊이 우선 탐색
def dfs (node, visited = None) :
  global cnt
  if visited is None :
    visited = set() # 방문한 정점 집합 생성
  
  visited.add(node) # 현재 정점 방문 처리
  answer[node] = cnt # 방문 순서 기록
  cnt += 1

  # 인접한 정점들 중 방문하지 않은 정점 재귀적으로 방문
  for neighbor in node_list[node] :
    if neighbor not in visited :
      dfs(neighbor, visited)


# DFS 실행 (시작 정점 R)
dfs(R)
# 1번 정점부터 N번 정점까지 방문 순서 출력
print(*answer[1:], sep='\n')





