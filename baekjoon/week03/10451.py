import sys
from collections import deque

input = sys.stdin.readline

def bfs(start_node, graph, visited):

    queue = deque([start_node])
    visited[start_node] = True  

    while queue:
        current_node = queue.popleft()
        next_node = graph[current_node]

        if not visited[next_node]:
            visited[next_node] = True 
            queue.append(next_node)    


t = int(input())

for _ in range(t):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    
    count = 0
    for i in range(1, n + 1):
        if not visited[i]:
            bfs(i, graph, visited) 
            count += 1        
            
    print(count)