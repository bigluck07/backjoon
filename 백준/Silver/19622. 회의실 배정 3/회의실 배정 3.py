import sys, math

n  = int(sys.stdin.readline().strip())
# 시작, 끝, 인원
ls = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

dp = [0 for _ in range(n)]

for i in range(n):
    if i==0:
        dp[i] = ls[i][2]
    elif i==1:
        dp[i] = max(ls[i][2], dp[i-1])
    else:
        dp[i] = max(dp[i-2]+ls[i][2], dp[i-1])
        
print(dp[n-1])