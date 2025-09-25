import sys
input = sys.stdin.readline
import heapq

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M) :
  start, end, cost = map(int, input().split())
  graph[start].append((end, cost))

def dijkstra(graph, start):
    distances = [float('inf')] * (N+1)
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # 이미 처리된 노드라면 스킵
        if current_distance > distances[current_node]:
            continue
        
        # 인접 노드 확인
        for neighbor, weight in graph[current_node] :
            distance = current_distance + weight
            
            # 더 짧은 경로를 찾았다면 갱신
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

start_node, end_node = map(int, input().split())

min_dis = dijkstra(graph, start_node)
print(min_dis[end_node])