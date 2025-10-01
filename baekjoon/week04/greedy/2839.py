N = int(input())

ans = -1
for five in range(N // 5, -1, -1):   # 5를 최대한 많이 쓰되 하나씩 줄여감
    remain = N - five * 5
    if remain % 3 == 0:
        three = remain // 3
        ans = five + three
        break

print(ans)
