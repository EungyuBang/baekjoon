import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
  # 1. 동전의 가지 수 N 입력
  N = int(input()) 
  
  # 2. 동전의 종류(액수) N개를 입력받아 리스트에 저장
  coins = list(map(int, input().split())) 
  
  # 3. 목표 금액 M (target_money) 입력
  target_money = int(input())
  
  # 4. DP 테이블 초기화
  # dp[i] = i원을 만들 수 있는 경우의 수
  dp = [0] * (target_money + 1)
  
  # 0원을 만드는 경우의 수는 1가지 (아무 동전도 사용하지 않음)
  dp[0] = 1

  # 5. DP 로직: 동전의 종류를 기준으로 외부 루프 실행
  for coin in coins:
      # 6. 금액을 기준으로 내부 루프 실행
      # 현재 동전(coin) 금액부터 목표 금액 M까지 순회
      for i in range(coin, target_money + 1):
          # 점화식: dp[i] = dp[i] + dp[i - coin]
          # i원을 만드는 기존 경우의 수에, (i - coin)원을 만드는 모든 경우의 수에
          # 현재 coin을 추가하는 새로운 경우의 수를 더해 누적합니다.
          dp[i] += dp[i - coin]

  # 7. 최종 결과 출력
  print(dp[target_money])