import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
# dpTable = [-1] * (N+1)

# def one(start):
#     if start == 1:
#         return 0
#     if dpTable[start] != -1:
#         return dpTable[start]

#     res = one(start - 1) + 1
#     if start % 2 == 0:
#         res = min(res, one(start // 2) + 1)
#     if start % 3 == 0:
#         res = min(res, one(start // 3) + 1)

#     dpTable[start] = res
#     return res

# print(one(N))
# -> 이거 메모리 초과남...



# dp[i] : 숫자 i를 1로 만드는 최소 연산 횟수
dp = [0] * (N + 1)

dp[1] = 0  # 1이면 연산 필요 없음

for i in range(2, N + 1):
    # 항상 -1 연산은 가능
    dp[i] = dp[i - 1] + 1
    # 2로 나누어 떨어지면
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    # 3으로 나누어 떨어지면
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])