import sys
input = sys.stdin.readline

T =int(input())


for _ in range(T) :
  vps = input().strip()
  stack = []
  empty = True
  for i in vps :
    if i == '(' :
      stack.append(i)
    else : # i = ')'
      if stack :
        stack.pop()
      else :
        empty = False
        break
    
  if empty and len(stack) == 0 :
    print('YES')
  else :
    print('NO')

'''  
input()만 쓰면 생기는 문제
Python에서 input()은 **줄 끝의 개행 문자(\n)**를 자동으로 제거하지만,
sys.stdin.readline()은 줄 끝에 개행 문자(\n)가 남아있음
-> .strip() - 문자열 앞/뒤의 공백과 개행 문자 제거
입력이 ()\n 에서 () 로 바뀜...
'''