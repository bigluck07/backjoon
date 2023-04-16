import sys

k = str(sys.stdin.readline().strip())
visited = [False] * len(k)


def solve(l, r):
    if l==r:
        return
    
    min_s = min(k[l:r])
    min_idx = k[l:r].index(min_s)+l
    visited[min_idx] = True
    
    for i in range(len(k)):
        if visited[i]:
            print(k[i], end="")
    print()
    
    solve(min_idx+1, r)
    solve(l, min_idx)    

solve(0, len(k))