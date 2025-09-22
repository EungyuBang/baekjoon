# 데이터 받아오는 법
# graph = [[] for _ in range(N+1)]
# a,b = map(int, input().split())
# graph[a].append(b)
# graph[b].append(a)


# dfs 기본형?
# visited = [False]
# def dfs(v) :
#   visited[v] = True
#   print(v, end='')
#   for i in graph[v] :
#     if not visited[i] :
#        dfs(i)