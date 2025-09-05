# T = int(input())

# for i in range(T) :
#   S,R = input().split() # 순서 잘 적어야 한다. 데이터가 반대로 들어옴...
#   for j in range(len(S)) :
#     print(S[j]*int(R), end='') 인덱스 번호로 뽑아서 곱함 
#   print()

T = int(input())

for _ in range(T) :
  R,S  = input().split() 
  for A in S :
    print(A*int(R),end='') # 그냥 바로 들어가서 하나하나 뽑아서 곱함
  print()