
import sys, copy
sys.setrecursionlimit(10**6)

m, n = map(int, sys.stdin.readline().strip().split())
mp = [[int(i) for i in str(sys.stdin.readline().strip())] for _ in range(m)]
hist = mp.copy()
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y):
    if (0 <= y < n) and (0 <= x < m) and hist[x][y] == 0:
        hist[x][y] = 2
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
            

for j in range(n):
    if hist[0][j] == 0:
        dfs(0, j)
        
print("YES" if 2 in hist[-1] else "NO")