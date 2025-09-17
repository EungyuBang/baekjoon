import sys
input = sys.stdin.readline

A, B, C = list(map(int, input().split()))


def num(A,B,C) :
  if B == 1 :
    return(A%C)

  half_B = num(A, B//2, C)

  if B % 2 == 0 :
    return (half_B * half_B) % C
  else :
    return (half_B * half_B * A) % C
  

print(num(A,B,C))



