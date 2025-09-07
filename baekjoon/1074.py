n, r, c = map(int, input().split())
answer = 0

while n != 0:
    n -= 1 # n = n - 1
    size = 2 ** n   # 현재 정사각형 한 변의 길이 -> 2의 n-1 이라 4등분됨 -> 길이는 절반

    # 좌표가 1사분면 (왼쪽 위)에 속할 때
    if r < size and c < size:
        pass  # 이동 없음

    # 좌표가 2사분면 (오른쪽 위)에 속할 때
    elif r < size and c >= size:
        answer += size * size        # 1사분면만큼 건너뜀
        c -= size                    # 열 좌표 보정 c = size - c

    # 좌표가 3사분면 (왼쪽 아래)에 속할 때
    elif r >= size and c < size:
        answer += size * size * 2    # 1, 2사분면 건너뜀
        r -= size                    # 행 좌표 보정 r = size - r

    # 좌표가 4사분면 (오른쪽 아래)에 속할 때
    else:
        answer += size * size * 3    # 1, 2, 3사분면 건너뜀
        r -= size
        c -= size                    # 행, 열 좌표 보정

print(answer)

