A, B = input().split()
# A = '123'
# B = '456'

C = list([A[2],A[1],A[0]])
D = list([B[2],B[1],B[0]])


E = "".join(C)
F = ''.join(D)

if C > D :
  print(int(E))
else :
  print(int(F))


# A, B = input().split()

# C = int(A[::-1])  # 문자열 뒤집어서 정수 변환
# D = int(B[::-1])

# if C > D:
#     print(C)
# else:
#     print(D)