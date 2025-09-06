# N = int(input())
# # 1~N 까지의 곱

# def factorial(N) : 음수로 가면 종료조건 N == 1 이 절대 만족되지 않아서 stack overflow 발생
#   if N == 1 :
#     return 1
#   else : 
#     return N * factorial(N-1) 

# result = factorial(N)
# print(result)



def factorial(n) :
  if n >= 1:
    return n * factorial(n-1) # 여기서 자기 자신을 다시 호출함
  else : 
    return 1

# 만약 n = 5라면
# factorial(5) :
#   return 5 * factorial(4) 여기서 함수 호출 5 * 4 * 3 * 2 * 1 (5)
#     factorial(4) :
#       return 4 * factorial(3) 여기서 함수 호출 4 * 3 * 2 * 1 (4)
#       factorial(3) :
#         return 3 * factorial(2) 여기서 함수 호출 3 * 2 * 1 (3)
#         factorial(2) :
#           return 2 * factorial(1)  여기서 함수 호출 2 * 1 (2)
#           factorial(1) : -> 1 (1)
#           return 1
# 쭉 내려가면서 함수 호출하고 조건 달성하면 다시 쭉 올라오면서 계산  
print(factorial(int(input())))