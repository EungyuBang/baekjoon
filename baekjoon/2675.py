# T = int(input())

# for i in range(T) :
#   S,R = input().split() # 순서 잘 적어야 한다. 데이터가 반대로 들어옴...
#   for j in range(len(S)) :
#     print(S[j]*int(R), end='') 인덱스 번호로 뽑아서 곱함 
#   print()



T = int(input())

for _ in range(T) :
  R, S = input().split()
  for x in S :
   print(x*int(R), end='') # -> end='' 줄바꿈 근데 모든 테스트 케이스를 한 줄로 내보냄
  print() # 이걸로 테스트 케이스들끼리 줄 바꿈
