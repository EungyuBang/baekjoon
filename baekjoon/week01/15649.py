N, M = map(int,input().split())

visited = [False] * (N + 1)
num_arr = []

def nums() :
  if len(num_arr) == M :
    print(*num_arr)
    return 
  for i in range(1, N+1) :
    if not visited[i] :
      visited[i] = True
      num_arr.append(i)
      nums()
      num_arr.pop()
      visited[i] = False

nums()

# num_arr → 리스트 그대로 출력
# *num_arr → 리스트 원소들을 풀어서 출력