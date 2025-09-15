import sys 

N = int(sys.stdin.readline())
num_list = []

for i in range(N) :
  num_list.append(int(sys.stdin.readline()))

num_list.sort()

for i in num_list :
  print(i)


# 이렇게하면 아주 조금 더 빠르긴함
#import sys
# # 빠른 입력을 위해 sys.stdin.readline 사용
# N = int(sys.stdin.readline())
# num_list = []
# for _ in range(N):
#     num_list.append(int(sys.stdin.readline()))
# num_list.sort()  # 오름차순 정렬
# # 빠른 출력
# for num in num_list:


# sys ~ 사용이유 : 주어진 N이 1 <= N <= 1,000,000 -> 범위 넓음 -> input() 으로 처리불가