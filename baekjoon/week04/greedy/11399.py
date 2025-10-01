# 그냥 정렬하고 하나씩 더하면 되는거 아님?

N = int(input())
time = list(map(int, input().split()))
time.sort()

sumList = [0] * N
sumList[0] = time[0]
for i in range(1, N) :
  sumList[i] = sumList[i-1] + time[i]
print(sum(sumList))

# 이전까지 누적된 결과에만 의존하므로 순차적으로 진행되면 된다. 