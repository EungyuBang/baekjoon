N = int(input())
A = list(map(int, input().split()))

dpTable = [1] * N

for i in range(N) :
  for j in range(i) :
    if A[j] < A[i] :
      dpTable[i] = max(dpTable[i], dpTable[j] + 1)
      
print(max(dpTable))