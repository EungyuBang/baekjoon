a = int(input())
b = int(input())


# print(a * b의 마지막 자리)
print(a * (b % 10))
# print(a * b의 두번째자리)
print(a * ((b%100) // 10))
# print(a * b 의 첫번째자리)
print(a * (b// 100))
print(a * b)