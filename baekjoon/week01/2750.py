N = int(input())
num_list = []

for i in range(N) :
  num_list.append(int(input()))

sorted_num = sorted(num_list)
for i in sorted_num :
  print(i)

# for i in sorted(num_list) :
#   print(i)

# sort() → 원본 리스트 자체를 정렬, 반환값 없음.
# sorted() → 원본은 그대로, 정렬된 새 리스트 반환.
# num_list = [4, 1, 3, 2]
# sorted_num = sorted(num_list)
# print(num_list)    # [4, 1, 3, 2]  <- 원본은 그대로
# print(sorted_num)  # [1, 2, 3, 4]  <- 새 리스트
