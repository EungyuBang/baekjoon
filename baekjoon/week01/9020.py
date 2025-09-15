def sosu(n): # 에라토스테네스의 체
    if n == 1:
        return False
    for i in range(2, int(n**0.5 + 1)): # 2 부터 n의 제곱근(int로 소수점 뗌) + 1
        if n % i == 0: # 위의 값으로 나눠서 나머지가 0이면 소수 x
            return False
    return True


for _ in range(int(input())):  # 테스트케이스를 이렇게 입력받을 수도 있음!
    n = int(input())

    a, b = n // 2, n // 2  # 입력받은 n을 반으로 쪼개 각각 a, b에 저장
    while a > 0:
        if sosu(a) and sosu(b):  # a와 b 둘 다 소수일 경우에 출력
            print(a, b)
            break  # break문을 안 넣었더니 반복문이 무한으로 출력되었음
        else:
            a -= 1  # 문제에서 작은 소수부터 출력하라고 했으므로 a는 1을 빼고, b는 1을 더한다.
            b += 1 