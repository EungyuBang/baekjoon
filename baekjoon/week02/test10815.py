import sys
input = sys.stdin.readline

N = int(input())
nums_list_n = list((map(int, input().split())))
nums_list_n.sort()

M = int(input())
nums_list_m = list(map(int, input().split()))


for i in nums_list_m:
    left, right = 0, N - 1
    num_found = False
    while left <= right:
        mid = (left + right) // 2
        if nums_list_n[mid] > i:
            right = mid - 1
        elif nums_list_n[mid] < i:
            left = mid + 1
        else:
            num_found = True
            print(1)
            break
    if num_found == False:
        print(0)
     


