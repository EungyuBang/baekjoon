import sys
sys.setrecursionlimit(10 ** 6) # 파이썬 -> 재귀 호출 횟수 제한 (1000) , -> 재귀 깊이를 100만으로 확장 (너무 큰 값으로 제한을 늘리면 스택 메모리 초과로 프로그램이 터질 수 있음)
input = sys.stdin.readline
node = []

while True :
    try :
        node.append(int(input()))
    except :
        break

def post_order(root_idx, last_idx):

    # 재귀 중단 조건
    if root_idx > last_idx:
        return

    # 루트 노드
    root = node[root_idx]

    # 오른쪽 서브트리의 시작 인덱스를 담을 변수
    right_start_idx = root_idx + 1

    while right_start_idx <= last_idx:
        # 루트 노드보다 큰 노드의 인덱스를 찾는다.
        if node[right_start_idx] > root:
            break
        right_start_idx += 1

    # 왼쪽 서브 트리 : 루트의 다음부터 ~ 루트보다 크지 않은 노드까지만
    post_order(root_idx + 1, right_start_idx - 1)

    # 오른쪽 서브 트리 : 루트보다 큰 노드부터 ~ 끝까지
    post_order(right_start_idx, last_idx)
    
    # 루트 출력
    print(root)


post_order(0, len(node) - 1) # 처음과 끝 인덱스를 초기값으로 함수를 호출한다.
