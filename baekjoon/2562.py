# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# f = int(input())
# g = int(input())
# h = int(input())
# i = int(input())


# arr = [a,b,c,d,e,f,g,h,i]
# maxValue = max(arr)
# maxValueNum = arr.index(maxValue)

# print(maxValue)
# print(maxValueNum)

nums = [int(input()) for _ in range(9)]
max_value = max(nums)
max_index = nums.index(max_value) + 1
# 인덱스 + 1 
print(max_value)
print(max_index)


