import sys                      # sys 모듈 불러오기 (빠른 입력을 위해)
input = sys.stdin.readline      # input() 대신 빠른 입력 함수로 설정

N = int(input())                # 정사각형 한 변의 길이 N 입력
num_list = [list(map(int, input().split())) for _ in range(N)]  # N×N 색종이 배열 입력
result = []                     # 최종 색종이 조각 색(0 또는 1)을 기록할 리스트

def count(x, y, N) :            # (x, y) 좌표에서 시작하는 N×N 영역을 검사하는 함수
  color = num_list[x][y]        # 해당 영역의 기준 색을 (왼쪽 위) 첫 칸 색으로 결정

  # 영역 전체를 순회하면서 기준 색과 다른 칸이 있는지 확인
  for i in range(x, x + N) :    # 행: x 부터 x+N-1 까지
    for j in range(y, y + N) :  # 열: y 부터 y+N-1 까지
      if color != num_list[i][j] :    # 만약 다른 색을 발견하면
        # 다른 색이 섞여 있으므로 현재 영역을 4등분해서 재귀 처리
        count(x, y, N//2)                    # 좌상단 (top-left)
        count(x, y + N//2, N//2)             # 우상단 (top-right)
        count(x + N//2, y, N//2)             # 좌하단 (bottom-left)
        count(x + N//2, y + N//2 , N//2)     # 우하단 (bottom-right)
        return                               # 한 번이라도 다른 색을 발견하면 더 이상 아래 코드로 내려오지 않음

  # 위의 for문을 끝까지 돌렸다면 '모두 같은 색' 이라는 뜻
  if color == 0 :
    result.append(0)  # 흰색이면 0을 추가
  else :
    result.append(1)  # 파란색이면 1을 추가

# 전체 영역(0,0)에서 시작하여 크기 N으로 검사 시작
count(0,0,N)

# 결과 리스트에서 0(흰색)과 1(파란색)의 개수를 세어 출력
print(result.count(0))
print(result.count(1))