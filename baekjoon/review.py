# 2557 
print("Hello World!")

# 10869
A,B = map(int, input().split())
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)

# 2588
A = int(input())
B = int(input())
print(A * (B % 10))          # 1의 자리
print(A * ((B // 10) % 10))  # 10의 자리
print(A * (B // 100))        # 100의 자리
print(A * B)

# 9498
score = int(input())
if score >= 90 :
  print('A')
elif score >= 80 :
  print('B')
elif score >= 70 :
  print('C')
elif score >= 60 :
  print('D')
else :
  print('F')

# 2753
year = int(input())
if year % 4 == 0 and year % 100 != 0 or year%400 == 0 : 
  print(1)
else :
  print(0)

# 1085 
x,y,w,h = list(map(int, input().split()))
nums = [x,y,h-y,w-x]
print(min(nums))

# 2739 
N = int(input())
for i in range(1,10) :
  print(N,'*', i ,'=', N*i)
  
# 10950
T = int(input())

for _ in range(T) :
  A,B = list(map(int, input().split()))
  print(A+B)

# 2438
N = int(input())
for i in range(1, N+1) : # 범위 잘 생각하기 !!!!
  print('*' *i)

# 10871
N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in A :
  if i < X :
    print(i)

# 2562 
nums = [int(input()) for _ in range(9)]
max_value = max(nums)
max_index = nums.index(max_value) + 1

print(max_value)
print(max_index)

# 8958 
T = int(input())
for _ in range(T) :
  OX = input()
  score = 0
  increment = 0
  for i in OX :
    if  i == 'O' :
      increment += 1
      score += increment
    else :
      increment=0
  print(score)

# 4344 
C = int(input())
for _ in range(C) :
  scores = list(map(int, input().split()))
  num = scores[0]
  case_num = scores[1:] # 인덱스 1번부터 끝까지 받아오겠다
  cnt = 0
  sum_score = sum(case_num)
  average = sum_score/num
  for i in case_num :
    if i > average :
      cnt += 1
  ratio = cnt/num * 100
  print("{:.3f}%".format(ratio)) # 소수점 셋째자리까지 , format -> {} 안에 넣겠다
# format (:.3f) → 무조건 반올림
# math.floor → 무조건 내림 (작은 쪽으로)
# math.ceil → 무조건 올림 (큰 쪽으로)
# math.trunc → 그냥 소수점 버림

# 2577
A = int(input())
B = int(input())
C = int(input())
mutifuly = A * B * C
counts = [0] * 10
for i in str(mutifuly) :
  counts[int(i)] += 1
for c in counts :
  print(c)

# 15596 
def solve(a) :
  value = sum(a)
  return(value)

# 11654 
a = input()
print(ord(a))

# 2675
T = int(input()) 
for _ in range(T) :
  R, S = input().split()
  for A in S :
    print(A*int(R),end='') # 그냥 바로 들어가서 하나하나 뽑아서 곱함
  print()

# 1152 
A = input()
B = A.split()
print(len(B))

# 2908
A,B = input().split()
C = list([A[2],A[1],A[0]])
D = list([B[2],B[1],B[0]])
E = ''.join(C)
F = ''.join(D)
if C > D :
  print(int(E))
else :
  print(int(F))

# 2869 
A,B,V = map(int, input().split())
days = (V-B)/(A-B)
if days == int(days) : # days가 소수점 뗀 days랑 같으면
  print(int(days)) # 그냥 날짜 반환
else :
  print(int(days) + 1) # days가 소수점 뗀 days 랑 다르면 -> 만약 days = 1.25 int(days) 는 1 -> 다름
                       # 하루 더 필요

# 1978 -> ** 반복문안에 뭐가 들어가야 하는지, 출력은 어디서 해야하는지에 대해 생각해보자 ** 
N = input()
nums = list(map(int, input().split()))
result = 0

for num in nums :
  cnt = 0 
  if num > 1 : 
    for i in range(2, int(num**0.5 +1)) :
      if num % i == 0 :
        cnt += 1
    if cnt == 0 : # 이건 나눠지는 수가 없으면 소수
      result += 1
print(result)

# N = input()
# nums = list(map(int, input().split()))
# result = 0

# for num in nums :
#   cnt = 0 
#   if num > 1 : 
#     for i in range(2, num+1) :
#       if num % i == 0 :
#         cnt += 1
#     if cnt == 1 : # 이건 나눠지는 수가 딱 한개면 소수
#       result += 1
# print(result)testtestt

# 9020
T = int(input())
def is_prime(n) :
  if n == 1 :
    return False 
  for i in range(2, int(n**0.5)+1) :
    if n % i == 0 :
      return False
  return True

for i in range(T) :
  n = int(input())
  a, b = n // 2, n // 2
  while a > 0 :
    if is_prime(a) and is_prime(b) :
      print(a,b)
      break
    else :
     a -= 1
     b += 1 

# 1065 
N = int(input())
cnt = 0

for i in range(1, N+1) :
  digits = list(map(int ,str(i))) 
# i는 정수 → 각 자리 수로 나누기 위해 문자열로 변환
# 각 자리 문자를 다시 정수로 → 계산 가능
# 최종적으로 [자리수1, 자리수2, ...] 리스트가 만들어짐
  if len(digits) <= 2 :
    cnt += 1 
  else : 
    if digits[2] - digits[1] == digits[1] - digits[0] :
      cnt += 1
print(cnt)

# 2628
width ,height = list(map(int, input().split())) 
num = int(input())
width_cut = [0, width] # 0-> 시작점 width-> 최대(끝)
height_cut = [0, height] # 0-> 시작점 height-> 최대(끝)

for i in range(num) :
  x,y = map(int, input().split())
  if x == 0 :
    height_cut.append(y)
  else :
    width_cut.append(y)

width_cut.sort()
height_cut.sort()

max_width = 0
for i in range(len(width_cut) - 1) :
  max_width = max(max_width, width_cut[i+1] - width_cut[i])

max_height = 0
for i in range(len(height_cut) - 1) :
  max_height = max(max_height, height_cut[i+1]-height_cut[i])

print(max_width * max_height)

# 10872 
n = int(input())
def factorial(n) :
  if n >= 1 :
    return n * factorial(n-1)
  else :
    return 1

print(factorial(n))

# 1914 
n = int(input())
def hanoi(n, s, e) :
  m = 6 - s - e

  if n == 1 :
    print(s,e)
  else :
    hanoi(n-1, s, m)
    print(s,e)
    hanoi(n-1, m, e)

print(2 ** n -1)
if n <= 20 :
  hanoi(n,1,3)

# 9663 n-queen

# 1074 z  
  

# 2750 
N = int(input())
num_list = []

for i in range(N) :
  num_list.append(int(input()))

sorted_num = sorted(num_list)
for i in sorted_num :
  print(i)

# sort() → 원본 리스트 자체를 정렬, 반환값 없음.
# sorted() → 원본은 그대로, 정렬된 새 리스트 반환.
# num_list = [4, 1, 3, 2]
# sorted_num = sorted(num_list)
# print(num_list)    # [4, 1, 3, 2]  <- 원본은 그대로
# print(sorted_num)  # [1, 2, 3, 4]  <- 새 리스트

# for i in sorted(num_list) :
#   print(i)


# 2751
import sys 

N = int(sys.stdin.readline())
num_list = []

for i in range(N) :
  num_list.append(int(sys.stdin.readline()))

num_list.sort()
for i in num_list :
  print(i)
