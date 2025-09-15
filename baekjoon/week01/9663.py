# N = int(input())
# N = 5

# row = [0] * N 
# cnt = 0

# def check(x) :
#   for i in range(x) :
#     if row[i] == row[x] or abs(row[i]- row[x]) == abs(x-i) : # 행 차이 == 열 차이 -> 대각선 
#       return False
#   return True
# # 여기까지 해서 같은줄 대각선 제거

# def queen(x) :
#   global cnt
#   if x == N :
#     cnt += 1
#     return
#   for i in range(N):
#     row[x] = i
#     if check(x) :
#       queen(x + 1)

# queen(0)
# print(cnt)

N = int(input())
cnt = 0

used_columns = [0] * N
used_diag1 = [False] * (2*N - 1)  # row + col
used_diag2 = [False] * (2*N - 1)  # row - col + (N-1)

def queen(row):
    global cnt
    if row == N:
        cnt += 1
        return
    for col in range(N):
        if not used_columns[col] and not used_diag1[row + col] and not used_diag2[row - col + N - 1]:
            # 퀸 놓기
            used_columns[col] = used_diag1[row + col] = used_diag2[row - col + N - 1] = True
            queen(row + 1)
            # 되돌리기
            used_columns[col] = used_diag1[row + col] = used_diag2[row - col + N - 1] = False

queen(0)
print(cnt)
