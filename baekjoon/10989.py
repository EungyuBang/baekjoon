import sys
N = int(sys.stdin.readline())
list = []

for i in range(N) :
  list.append(int(sys.stdin.readline()))

list.sort()

for i in list :
  sys.stdout.write(i)