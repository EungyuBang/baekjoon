C = int(input())
for _ in range(C) :
  data = list(map(int, input().split()))
  # 5 50 60 70 80 90
  N = data[0] # 5 
  scores = data[1:] # 점수들 ~ scores = [50,60,70,80,90]
  sumNums = sum(scores) # 점수들 합 350 
  average = sumNums / len(scores) # 점수들 평균
  count = 0
  for i in scores :
   if i > average :
     count += 1
  ratio = count/N * 100
  print("{:.3f}%".format(ratio)) # 소수점 셋째 자리까지 출력


# c = int(input())
# for _ in range(c) :
#   scores = list(map(int, input().split()))
#   case_num = scores[1:]
#   A = sum(case_num)/len(case_num) # 평균
#   cnt = 0
#   for i in case_num :
#     if i > A :
#       cnt += 1
#   C = cnt/len(case_num) * 100
#   print('{:.3f}%'.format(C))

    