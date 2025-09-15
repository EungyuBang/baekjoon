N = int(input())
words = list((input() for _ in range(N)))

words = list(set(words)) # set -> 중복 단어 제거
words.sort() # -> 사전순으로 정렬
words.sort(key=len) # -> 길이 기준으로 정렬

for i in words :  
  print(i)