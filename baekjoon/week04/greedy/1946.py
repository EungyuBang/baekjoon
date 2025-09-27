# 면접 혹은 서류가 무조건 다른 지원자보다 높아야함
# 이러면 면접, 서류 1등은 무조건 합격 -> 같은 사람일수도 다른사람일수도
# 서류 기준 정렬 -> 첫번째는 무조건 합격
import sys
input = sys.stdin.readline

T = int(input())


for _ in range(T) :
  ranking = []
  N = int(input())
  for __ in range(N) :
    docRank , itvRank = map(int, input().split())
    ranking.append((docRank, itvRank))
  ranking.sort()
  # 처음엔 서류 1등보다 면접 순위가 높아야함 -> 기준점 -> 서류 1등의 면접 순위
  # 이후 standardItv 초기화 해줘야함
  cnt = 1
  standardItv = ranking[0][1]
  for i in range(1, N) :
    if ranking[i][1] < standardItv :
      cnt += 1
      standardItv = ranking[i][1]
  print(cnt)
