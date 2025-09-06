width, height = map(int,input()) # 종이의 가로 세로 길이 10 8
num = int(input())
width_cut = [0,width] # 가로 자르기 -> 세로 길이 분할 (가로로 자르면 세로 길이에 영향) [0, 10]
height_cut = [0,height] # 세로 자르기 -> 가로 길이 분할 (세로로 자르면 가로 길이에 영향) [0, 8]

for _ in range(num) :
    x,y = map(int,input().split()) #입력된 값 공백 기준으로 나누고 0 3 , 1 4
    if x == 0 : # 만약 처음 들어온 값이 0 이다 -> y는 가로를 자르는 기준선 -> 세로에 영향을 줌  [0, 8, 3]
        height_cut.append(y) # -> 그래서 들어온 값을 계속 height_cut 에 넣어줌
    else : # 만약 처음 들어온 값이 0이 아니다 -> 1 -> y는 세로를 자르는 기준선 -> 가로에 영향을 줌
        width_cut.append(y) # -> 들어온 값을 계속 width_cut에 넣어줌 -> [0,10,4]


width_cut.sort() # [0, 4, 10]
height_cut.sort() # [0, 3, 8]

max_width = 0
for i in range(len(width_cut)-1) :
    max_width = max(max_width, width_cut[i+1] - width_cut[i]) 

# width_cut[i+1] - width_cut[i] 계산 → 값 예: 4
# max_width의 현재 값 확인 → 예: 0
# max(0, 4) → 4 반환
# = 연산 → max_width 변수에 4 저장
# 다음 반복:
# width_cut[i+1] - width_cut[i] 계산 → 값 예: 6
# max_width 현재 값 확인 → 4
# max(4, 6) → 6 반환
# = 연산 → max_width 변수에 6 저장

max_height = 0
for i in range(len(height_cut)-1) :
    max_height = max(max_height, height_cut[i+1] - height_cut[i])

print(max_height * max_width)



# width, height = map(int, input().split())  # 종이 가로 세로
# num = int(input())

# width_cut = [0, width]
# height_cut = [0, height]

# for _ in range(num):
#     x, y = map(int, input().split())
#     if x == 0:   # 가로 자르기 → 세로 분할
#         height_cut.append(y)
#     else:        # 세로 자르기 → 가로 분할
#         width_cut.append(y)

# width_cut.sort()
# height_cut.sort()

# max_width = max(width_cut[i+1] - width_cut[i] for i in range(len(width_cut)-1))
# max_height = max(height_cut[i+1] - height_cut[i] for i in range(len(height_cut)-1))

# print(max_width * max_height)
