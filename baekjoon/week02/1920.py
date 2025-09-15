import sys
input = sys.stdin.readline

N = int(input())
N_nums = set(map(int, input().split())) # set -> 중복제거 + 순서 없음
M = int(input())
M_nums = list(map(int, input().split())) # 입력받은 그대로 출력해야해서 list 사용

for i in M_nums :
  if i in N_nums :
    print(1)
  else :
    print(0)
