A,B,V = map(int,input().split())

# A, B, V = map(int, input().split())
# n = 1
# while True: -> 시간 초과로 실패
#     # n일째 올라간 총 높이 계산
#     if n * A - (n - 1) * B >= V:
#         break
#     n += 1

# print(n)

day = (V-B)/(A-B)
if day == int(day) :
  print(int(day))
else:
  print(int(day) + 1)