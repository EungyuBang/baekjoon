import sys
input = sys.stdin.readline  # 입력 속도를 빠르게 하기 위해 sys.stdin.readline 사용

stack = []  # 스택을 저장할 리스트 초기화
n = int(input())  # 명령어 개수 입력, n은 총 수행할 명령어 수

for _ in range(n):  # n번 반복하며 명령어 처리
    cmd = input().split()  # 명령어를 공백 기준으로 분리, cmd[0]은 명령어, cmd[1]은 값(있으면)

    if cmd[0] == "push":  # 명령어가 push일 때
        stack.append(int(cmd[1]))  # 스택 맨 뒤에 값 추가

    elif cmd[0] == "pop":  # 명령어가 pop일 때
        print(stack.pop() if stack else -1)  
        # 스택이 비어있지 않으면 마지막 값을 제거하고 출력
        # 비어있으면 -1 출력

    elif cmd[0] == "size":  # 명령어가 size일 때
        print(len(stack))  # 현재 스택에 들어있는 요소 개수 출력

    elif cmd[0] == "empty":  # 명령어가 empty일 때
        print(0 if stack else 1)  
        # 스택이 비어있으면 1, 아니면 0 출력

    elif cmd[0] == "top":  # 명령어가 top일 때
        print(stack[-1] if stack else -1)  
        # 스택 맨 위 값 출력, 비어있으면 -1 출력

stack = []
n = int(input())

for _ in range(n) :
    cmd = input().split()

    if cmd[0] == 'push' :
        stack.append(int(cmd[1]))
    elif cmd[0] == 'pop' :
        print(stack.pop() if stack else -1)
    elif cmd[0] == 'size' :
        print(len(stack))
    elif cmd[0] == 'empty' :
        print(0 if stack else 1)
    elif cmd[0] == 'top' :
        print(stack[-1] if stack else -1)