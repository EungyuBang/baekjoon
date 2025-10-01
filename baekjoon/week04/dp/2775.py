T = int(input())

for _ in range(T) :
  k = int(input())
  n = int(input())

  dpTable = [[0] * (n+1) for _ in range(k+1)]
  
