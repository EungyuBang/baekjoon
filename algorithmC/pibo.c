#include <stdio.h>
#include <stdlib.h>

int main() {
  int N;
  scanf("%d", &N);

  if(N == 1) {
    printf("1\n");
    return 0;
  }
  if(N == 2) {
    printf("2\n");
    return 0;
  }
  
  long long *dp = (long long*)calloc(N+1, sizeof(long long));

  if(dp == NULL) {
    return 1;
  }

  dp[0] = 0;
  dp[1] = 1;

  for (int i = 3 ; i <= N ; i++) {
    dp[i] = dp[i-2] + dp[i-1];
  }
  printf("%lld\n", dp[N]);
  free(dp);

  return 0;
}