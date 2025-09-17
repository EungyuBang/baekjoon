import sys
input = sys.stdin.readline

while True:
    stc = input().rstrip()  # 줄 끝 \n 제거
    if stc == '.':          # 종료 조건
        break

    stack = []
    is_balanced = True      # 균형 체크 변수

    for x in stc:
        if x == '(' or x == '[':
            stack.append(x)
        elif x == ')':
            if not stack or stack[-1] != '(':
                is_balanced = False
                break
            stack.pop()
        elif x == ']':
            if not stack or stack[-1] != '[':
                is_balanced = False
                break
            stack.pop()

    if is_balanced and len(stack) == 0:
        print('yes')
    else:
        print('no')
