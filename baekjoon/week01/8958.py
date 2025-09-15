T = int(input())

for _ in range(T):
  quiz_result = input() # 퀴즈 결과 oxoxoxoxo
  score = 0
  consecutive = 0
  for i in quiz_result :
    if i == 'O' :
      consecutive += 1 # OOO -> 1 2 3
      score += consecutive # score = score + consecutive -> 실질적은 숫자 증가는 consecutive 에서 
    else :
      consecutive = 0 # OOOX -> 1 2 3 0 (초기화 해줌)
  print(score)
