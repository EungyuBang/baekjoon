import sys             # 빠른 입력을 위해 sys 모듈 임포트
import heapq           # 힙 자료구조를 사용하기 위해 heapq 모듈 임포트

input = sys.stdin.readline  # 입력 속도를 빠르게 하기 위해 sys.stdin.readline 사용

heap = []               # 힙을 저장할 리스트 초기화 (최대 힙 구현 예정)
n = int(input())        # 명령어(입력) 개수 입력, n은 총 입력 줄 수

for _ in range(n):      # n번 반복하며 각 입력 처리
    x = int(input())    # 각 줄 입력을 정수로 변환
    
    if x > 0:           # 입력 값이 0보다 크면 → 힙에 추가(push)
        heapq.heappush(heap, -x)  
        # 최대 힙을 구현하기 위해 값에 음수를 붙여 최소 힙에 저장
        # 예: 5를 넣으면 -5 저장 → 가장 작은 값(-5)이 실제 최대값 5가 됨
    else:               # 입력 값이 0이면 → 힙에서 최대값 출력 후 제거
        print(-heapq.heappop(heap) if heap else 0)  
        # heap이 비어있지 않으면 heappop()으로 최소값(-최대값) 제거 후 다시 음수로 변환해 출력
        # heap이 비어있으면 0 출력
