# 5원으로 나누고 2원으로 나누고 

import sys
input = sys.stdin.readline

n = int(input()) # 13

# if n % 5 % 2 == 0 :
#   five = n // 5
#   two = (n % 5) // 2
#   print(five + two)
# else :
#   print(-1)
# 반례생김 -> 13 -> 5원 하나에 2원 3개 이런경우

# 반복문으로 5원을 하나씩 빼면서?
if n % 5 == 0:
    print(n // 5)
else:
    five = n // 5
    while five >= 0:
        minusFive = n - five * 5
        if minusFive % 2 == 0:
            print(five + minusFive // 2)
            break
        five -= 1
    else:  
        print(-1)