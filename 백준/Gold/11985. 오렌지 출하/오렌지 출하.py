import sys, math

# 갯수, 박스당 개수, 포장비
input = sys.stdin.readline
n,m,k  = map(int, input().strip().split())
ls = [0] + [int(input()) for _ in range(n)]

# i 번째 오렌지까지 포장 최소 비용
dp = [0]*(n+1)
dp[1] = k

# cost = k + 박스안갯수*(큰애-작은애)
for i in range(2, n+1):
    min_v = max_v = ls[i]
    
    dp[i] = dp[i-1]+k
    for s in range(2, min(m, i)+1):
        j = i - s + 1 # box 가장 왼쪽 오렌지 

        min_v, max_v = min(min_v, ls[j]), max(max_v, ls[j])
        
        box_cost = k+s*(max_v-min_v)
        
        dp[i] = min(dp[i], dp[j-1]+box_cost)
        
print(dp[n])