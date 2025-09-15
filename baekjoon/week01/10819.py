import sys
input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline 사용

N = int(input())  # 숫자 개수 입력
nums = list(map(int, input().split()))  # 숫자 리스트 입력
visited = [False] * N  # 각 숫자 사용 여부를 저장하는 리스트

# 인접한 원소의 차이의 절댓값 합을 계산하는 함수
def sum_nums(A) :
    return sum(abs(A[i] - A[i+1]) for i in range(N-1))

max_value = 0  # 최대값을 저장할 변수

# 순열을 생성하며 최대값을 찾는 백트래킹 함수
def backtrack(curr):
    global max_value
    # 모든 숫자를 다 선택했을 때
    if len(curr) == N:
        max_value = max(max_value, sum_nums(curr))  # 최대값 갱신
        return
    # 아직 선택하지 않은 숫자를 하나씩 선택
    for i in range(N):
        if not visited[i]:  # i번째 숫자를 아직 사용하지 않았다면
            visited[i] = True  # 사용 표시
            curr.append(nums[i])  # 순열에 숫자 추가
            backtrack(curr)  # 다음 숫자 선택을 위해 재귀 호출
            curr.pop()  # 재귀 후 숫자 제거 (다른 순열 탐색)
            visited[i] = False  # 사용 표시 해제 (백트래킹)


# 백트래킹 재귀 과정
# for i in range(N) → nums의 모든 숫자를 시도
# if not visited[i] → 아직 선택하지 않은 숫자만 사용
# visited[i] = True → nums[i] 선택 표시
# curr.append(nums[i]) → 순열에 숫자 추가
# backtrack(curr) → 재귀 호출, 다음 숫자 선택
# curr.pop() → 재귀 후 숫자 제거 (다른 순열 탐색)
# visited[i] = False → 재귀 후 선택 해제

backtrack([])  # 순열 생성을 시작
print(max_value)  # 최대값 출력

# --- 재귀(백트래킹)로 순열을 만들어 푸는 또 다른 예시 ---
max_ans = 0
used = [False] * N

def recur(path):
    global max_ans
    if len(path) == N:
        total = sum(abs(path[i] - path[i+1]) for i in range(N-1))
        max_ans = max(max_ans, total)
        return
    for i in range(N):
        if not used[i]:
            used[i] = True
            path.append(nums[i])
            recur(path)
            path.pop()
            used[i] = False

recur([])
print(max_ans)