# greedy
# 우선 - 를 기준으로 나눠 -> - 뒤에 있는 거 다 빼 
import sys
input = sys.stdin.readline

form = input().strip()

split_ = form.split('-')

result = 0

first_num = split_[0].split('+')
for num_str in first_num :
  result += int(num_str)

for term in split_[1:] :
  sub_num = term.split('+')
  term_sum = 0
  for num_str in sub_num :
    term_sum += int(num_str)

  result -= term_sum

print(result)
