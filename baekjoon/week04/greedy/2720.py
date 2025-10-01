# 큰거부터 나눠서 몫은 배열에 넣고 나머지는 더 나누기
import sys
input = sys.stdin.readline

T = int(input())
nums = [int(input()) for _ in range(T)]

changeMoney = [[0] * 4 for _ in range(T)]

for i in range(T) :
  changeMoney[i][0] = nums[i] // 25
  changeMoney[i][1] = (nums[i] % 25) // 10
  changeMoney[i][2] = (nums[i] % 25 % 10) // 5
  changeMoney[i][3] = (nums[i] % 25 % 10 % 5) // 1

for i in changeMoney :
  print(*i)