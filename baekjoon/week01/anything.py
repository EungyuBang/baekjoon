N = int(input())
cnt = 0
for i in range(1, N+1) :
  digits = list(map(int ,str(i))) 
  if len(digits) <= 2 :
    cnt += 1
  else :
    if digits[2] - digits[1] == digits[1] - digits[0] :
      cnt += 1
print(cnt)