# 배열 안에서 2개의 인덱스 더해서 target 이면 그 두 놈 제외하고 print

# height_nums = [int(input()) for _ in range(9)]

# total = sum(height_nums)
# target = total - 100 

# remove_i, remove_j = -1, -1

# for i in range(len(height_nums)):
#     for j in range(i+1, len(height_nums)):  # i < j 로 범위 제한
#         if height_nums[i] + height_nums[j] == target:
#             remove_i, remove_j = i, j
#             break
#     if remove_i != -1:   # 찾았으면 바깥 for도 종료
#         break
    
# # pop은 뒤에서부터 해야 인덱스가 안 꼬임 (j가 더 크니까)
# height_nums.pop(remove_j)
# height_nums.pop(remove_i)

# height_nums.sort()


# for x in height_nums :
#     print(x)


