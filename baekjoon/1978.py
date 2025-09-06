N = input()
nums = list(map(int, input().split()))
result = 0

for num in nums :
  cnt = 0
  if num > 1 : # 1은 소수에서 제외니까
    for i in range(2, num + 1) :
      if num % i == 0 : # num에 들어온 숫자를 2 ~ num + 1 사이의 모든 숫자로 나눔 -> 그래서 나머지가 0 이면 카운트
           cnt += 1 # 나머지가 0일때 마다 카운트
    if cnt == 1 : # 나머지에 0이 하나면 1을 제외하고 본인을 0으로 만드는게 자기 자신 하나뿐 -> 소수 
        result += 1
print(result)
