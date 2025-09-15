# N = input()
# N = '100'
# A = int(N[0])
# B = int(N[1])
# C = int(N[2])
# D = int(N)

# cnt = 0

# for i in range(1, D+1) :
#   if i == (2 * B == A + C or A == B == C) :
#    cnt += 1

# print(cnt)

N =int(input())
cnt = 0

for i in range(1, N+1) :
  str_num = str(i)
  digits = list(map(int, str_num))
  if len(digits) <= 2:  # 1자리, 2자리 숫자는 무조건 한수
    cnt += 1
  else : 
    if digits[1] - digits[0] == digits[2] - digits[1] :
      cnt += 1
print(cnt)