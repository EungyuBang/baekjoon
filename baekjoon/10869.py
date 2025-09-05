A, B = map(int, input().split())
# 사용자가 10 20 입력하면 input().split() -> 가운데 공백을 기준으로 ['10','20']이 됨 -> A, B = map(int, ['10','20'])
# A, B = map(int, ['10','20']) 문자열인 '10', '20' 을 int를 통해 정수로 변환 
print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
