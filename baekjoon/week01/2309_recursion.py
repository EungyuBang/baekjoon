# 9명의 난쟁이 키 입력 (한 줄씩)
heights = [int(input()) for _ in range(9)]

N = 9  # 난쟁이 수
target = 100  # 키 합 목표값
chosen = []  # 선택된 난쟁이 키를 저장할 리스트

# 백트래킹 함수: 7명을 선택하여 키 합이 100이 되는 조합 찾기
def backtrack(start, curr_sum) :
    # 탈출조건: 7명을 선택했을 때
    if len(chosen) == 7 :
        if curr_sum == target :  # 키 합이 100이면
            for h in sorted(chosen) :  # 오름차순 출력
                print(h)
            exit()  # 정답을 찾으면 프로그램 종료
        return  # 합이 100이 아니면 리턴
    
    # 인덱스가 범위를 벗어나면 리턴
    if start >= N :
        return
    
    # start부터 N까지 반복하며 난쟁이 선택
    for i in range(start, N) :
        chosen.append(heights[i])  # i번째 난쟁이 선택
        backtrack(i+1, curr_sum + heights[i])  # 다음 난쟁이 선택 (재귀)
        chosen.pop()  # 백트래킹: 선택 취소
    
backtrack(0,0)  # 탐색 시작

# 아래는 백트래킹 탐색 과정 예시(트리 구조 설명)
# start=0, chosen=[]
# └─ append(20) -> chosen=[20]   ← start=0
#     └─ append(7) -> chosen=[20,7]  ← start=1
#         └─ append(23) -> chosen=[20,7,23] ← start=2
#             └─ append(19) -> chosen=[20,7,23,19] ← start=3
#                 └─ append(10) -> chosen=[20,7,23,19,10] ← start=4
#                     ├─ append(15) -> [20,7,23,19,10,15]  # depth=5
#                     │   ├─ append(25) -> fail → pop(25) → [20,7,23,19,10,15]
#                     │   ├─ append(8) -> fail → pop(8)
#                     │   └─ append(13) -> fail → pop(13)
#                     │   ← pop(15) → chosen back to [20,7,23,19,10]
#                     ├─ append(25) -> [20,7,23,19,10,25]
#                     │   ├─ append(8) -> fail → pop(8)
#                     │   └─ append(13) -> fail → pop(13)
#                     │   ← pop(25) → chosen back to [20,7,23,19,10]
#                     └─ append(8) -> [20,7,23,19,10,8]
#                         └─ append(13) -> [20,7,23,19,10,8,13] ✅ FOUND
