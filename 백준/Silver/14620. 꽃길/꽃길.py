
import sys

n = int(sys.stdin.readline().strip())
area = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
total = 0
ans = 99999999

dirt = [(0,0),(-1,0),(1,0),(0,-1),(0,1)]

def check_visited(x,y):
    for i,j in dirt:
        a = x+i
        b = y+j
        if visited[a][b]==1:
            return 0
    return 1


def dfm(cnt):
    global total, ans
    if cnt == 3:
        ans = min(ans, total)
        return
    
    for x in range(1, n-1):
        for y in range(1, n-1):
            if check_visited(x,y):
                for i,j in dirt:
                    a = x+i
                    b = y+j
                    visited[a][b]=1
                    total += area[a][b]
            
                dfm(cnt+1)

                for i,j in dirt: # 재귀를 위해 원복
                    a = x+i
                    b = y+j
                    visited[a][b]=0
                    total -= area[a][b]      
dfm(0)
print(ans)