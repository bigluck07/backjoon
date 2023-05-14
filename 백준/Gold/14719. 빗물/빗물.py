import sys, math, copy

h,w  = map(int, sys.stdin.readline().strip().split())
mp = list(map(int, sys.stdin.readline().strip().split()))
block = [[0]*w for _ in range(h)]
for y in range(w):
    for x in range(mp[y]):
        block[x][y] = 1

answer = 0
for i in range(h):
    strt = False
    s = 0
    for j in range(w):
        if block[i][j] == 1:
            if strt == True and s>0:
                answer+=s
                s=0
            strt = True
        elif strt == True:
            s+=1
            
print(answer)