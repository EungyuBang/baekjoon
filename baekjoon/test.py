'''
스레드는 한몸이다
스레드가 죽으면 프로세스 전체가 죽는다
보안에서 취약 할 수 있음
스레드가 빠르고 경량이어서 많은 상황에서 멀티스레드는 유리하지만 (메모리 공유 good but 보안 취약)
안정성이 중요한 시스템에서는 단점이 될 수도 있다.
'''

'''
프로그래밍의 요소
Primitive expression
means of combination
means of abstraction
'''
'''
def p() :
  while tue : pass

def test(x,y) :
  return 0 if x == 0 else y

test(o,p())
'''

'''
def nsum(n) :
  total  = 0
  for i in range(n+1) :
    total += 1
  return total
'''

# recursion - 부메랑, 어느 시점에서 브레이크를 걸었을때 답을 얻지 못하는 시점이 있다, 중복계산이 많다 , 많이 해봐야한다...
# tail recursion - 자기 자신만 호출(수식X)

'''
def expoenen(x,n) :
  if x == 0 :
    return 1
  elif x % 2 == 0 :
    return x * expoenen(x, n//2) * expoenen(x, n//2)
  elif x % 2 == 1:
    return x * expoenen(x, n//2) * expoenen(x, n//2 - 1)
  
'''
# 언어가 사람의 사고를 제한시킨다