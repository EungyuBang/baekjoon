N = int(input())
nums = list(map(int,input().split()))
nums.sort()

left_idx = 0
right_idx = N - 1
result = [nums[left_idx],nums[right_idx]]
best_sum = abs(nums[left_idx] + nums[right_idx])

while left_idx < right_idx :
  left_num = nums[left_idx]
  right_num = nums[right_idx]
  sum_nums = left_num + right_num
  if abs(sum_nums) < best_sum :
    best_sum = abs(sum_nums)
    result = [left_num, right_num]
    if best_sum == 0 :
      break

  if sum_nums < 0 :
    left_idx += 1
  else :
    right_idx -= 1
  
print(result[0], result[1])








# best_num = (0,0)

# left, right = nums[0], nums[-1]

# while left <= right :
#   s = left + right
#   for i in range(len(nums)) :
#     if nums[i] + nums[-(i + 1)] == 0 :
