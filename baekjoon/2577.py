A = int(input())
B = int(input())
C = int(input())

multifly = A * B * C

# count0 = 0
# count1 = 0
# count2 = 0 ~
# for i in str(multifly) : 
#   if i == '0' :
#     count0 += 1
#   elif i == '1' :
#     count1 += 1
#   elif ~
# print(count0)
# print(count1) 이렇게 하면 가능하지만 너무 길어짐 -> 무조건 다른 방법있겠다 싶어서 찾아봄


#  0~9 숫자 개수를 저장할 리스트 생성
counts = [0] * 10  
# counts 리스트는 [0,0,0,0,0,0,0,0,0,0] 으로 초기화
# 인덱스 번호가 숫자를 의미: counts[0] = 0의 개수, counts[1] = 1의 개수, ..., counts[9] = 9의 개수

#  곱한 수를 문자열로 바꿔서 각 자리 숫자를 반복
for i in str(multifly):
    # i는 문자열: '1', '7', '0', '3', '7', '3', '0', '0' 순서
    counts[int(i)] += 1  
    # int(i) → 문자열 숫자를 정수로 변환
    # 예: i='2' → int(i)=2 → counts[2] += 1
    # 즉, 리스트에서 해당 숫자 위치의 값이 1 증가
    # 리스트 자체가 같은 객체이므로, 값이 누적됨

#  0~9 숫자의 개수 출력
for c in counts:
    print(c)  # 순서대로 counts[0], counts[1], ..., counts[9] 출력