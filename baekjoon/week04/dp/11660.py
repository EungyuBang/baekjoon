import sys
input = sys.stdin.readline

N , M = map(int, input().split())

numList = [list(map(int, input().split())) for _ in range(N)]

coord = [list(map(int, input().split())) for _ in range(M)]

print(numList)
print(coord)