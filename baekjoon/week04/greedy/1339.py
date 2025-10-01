# 반복문 두개 돌리면서 숫자 인덱스로 접근하면서 가중치 배정
# 가중치에 따라서 숫자 배정
# 곱하고 더해
N = int(input())
words = [input().strip() for _ in range(N)]

weights = {}

for word in words :
  wordLength = len(word) 
  for i in range(wordLength) : 
    alphabet = word[i]
    value = 10 ** (wordLength - i -1)
    weights[alphabet] = weights.get(alphabet, 0) + value 

sortWeights = sorted(weights.items(), key=lambda x: x[1] , reverse=True)

nums = 9
alphabetToNum = {}
for j in sortWeights :
  alphabetToNum[j[0]] = nums
  nums -= 1

sumNums = 0
for alpha, weight in weights.items() :
  sumNums += weight * alphabetToNum[alpha]

print(sumNums)