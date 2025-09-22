# 가중치가 있는 간선을 최소로 모든 노드를 순회 -> 최소 신장 트리

import sys
input = sys.stdin.readline

V, E = map(int, input().split())

edges = []

for _ in range(E) :
  a,b,c = map(int, input().split())
  edges.append((c,a,b)) #(가중치, a, b)

edges.sort()

parent = [i for i in range(V + 1)]

def find(x) :
  if parent[x] != x : 
    parent[x] = find(parent[x])
  return parent[x]

def union(a,b) :
  a_root = find(a)
  b_root = find(b)
  if a_root != b_root :
    parent[b_root] = a_root
    return True
  return False

result = 0
for cost, a, b in edges :
  if union(a, b) :
    result += cost

print(result)

