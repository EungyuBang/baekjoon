T = int(input())

for _ in range(T):
  quiz_result = input() # 큐ㅟ즈 결과 oxoxoxoxo
  score = 0
  consecutive = 0

  for i in quiz_result :
    if i == 'O' :
      consecutive += 1
      score += consecutive
    else :
      consecutive = 0
  print(score)
