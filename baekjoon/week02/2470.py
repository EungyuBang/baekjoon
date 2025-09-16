N = int(input())  # 전체 숫자 개수 입력
nums = list(map(int,input().split()))  # N개의 정수 입력받아 리스트로 저장
nums.sort()  # 투 포인터를 사용하기 위해 정렬 (오름차순)

# 투 포인터 초기 위치 설정
left_idx = 0              # 왼쪽 포인터 (리스트 맨 앞)
right_idx = N - 1         # 오른쪽 포인터 (리스트 맨 끝)

# 초기값: 가장 양 끝 두 수를 결과로 설정
result = [nums[left_idx], nums[right_idx]]
best_sum = abs(nums[left_idx] + nums[right_idx])  
# 현재 두 수의 합 절댓값을 최소값 후보로 저장

# 투 포인터 탐색 시작
while left_idx < right_idx:  # 두 포인터가 교차하기 전까지 반복
    left_num = nums[left_idx]   # 왼쪽 값
    right_num = nums[right_idx] # 오른쪽 값
    sum_nums = left_num + right_num  # 두 수의 합

    # 현재 합이 지금까지의 best_sum보다 0에 더 가깝다면 갱신
    if abs(sum_nums) < best_sum:
        best_sum = abs(sum_nums)
        result = [left_num, right_num]  # 결과값 갱신
        if best_sum == 0:  # 합이 0이면 더 이상 탐색할 필요 없음
            break

    # 합이 음수라면 → 왼쪽 값을 키워야 0에 가까워짐
    if sum_nums < 0:
        left_idx += 1
    # 합이 양수라면 → 오른쪽 값을 줄여야 0에 가까워짐
    else:
        right_idx -= 1

# 최종 결과 출력 (합이 0에 가장 가까운 두 수)
print(result[0], result[1])








# best_num = (0,0)

# left, right = nums[0], nums[-1]

# while left <= right :
#   s = left + right
#   for i in range(len(nums)) :
#     if nums[i] + nums[-(i + 1)] == 0 :
