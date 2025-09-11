# 외판원 순회2 (백준 10971)
N = int(input())  # 도시의 개수 입력

cost = [list(map(int, input().split())) for _ in range(N)]  # 각 도시 간 이동 비용 입력 (2차원 리스트)

visited = [False] * N  # 각 도시 방문 여부를 저장하는 리스트
min_cost = float('inf')  # 최소 비용을 저장할 변수, 초기값은 무한대

# DFS로 모든 경로를 탐색하는 함수
def dfs(start, now, cnt, total):
    global min_cost
    # 모든 도시를 방문했고, 시작 도시로 돌아갈 수 있을 때
    if cnt == N and cost[now][start]:
        min_cost = min(min_cost, total + cost[now][start])  # 최소 비용 갱신
        return
    # 다음 방문할 도시를 선택
    for next in range(N):
        # 아직 방문하지 않았고, 현재 도시에서 next 도시로 갈 수 있을 때
        if not visited[next] and cost[now][next]:
            visited[next] = True  # next 도시 방문 표시
            dfs(start, next, cnt + 1, total + cost[now][next])  # 다음 도시로 이동
            visited[next] = False  # 백트래킹: 방문 표시 해제

# 모든 도시를 시작점으로 하여 탐색 (순회 경로가 달라질 수 있음)
for i in range(N):
    visited[i] = True  # 시작 도시 방문 표시
    dfs(i, i, 1, 0)  # DFS 탐색 시작
    visited[i] = False  # 방문 표시 해제
print(min_cost)  # 최소 비용 출력