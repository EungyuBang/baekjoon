import sys
input = sys.stdin.readline

money = int(input())

changeMoney = 1000 - money

a = 500
b = 100
c = 50
d = 10
e = 5
f = 1

arr = [0] * 6


arr[0] = changeMoney // a
changeMoney %= a
arr[1] = changeMoney // b
changeMoney %= b
arr[2] = changeMoney // c
changeMoney %= c
arr[3] = changeMoney // d
changeMoney %= d
arr[4] = changeMoney // e
changeMoney %= e
arr[5] = changeMoney // f

print(sum(arr))