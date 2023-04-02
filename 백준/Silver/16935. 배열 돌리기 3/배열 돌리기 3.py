import sys, math, copy

n,m,r  = map(int, sys.stdin.readline().strip().split()) # n*m, 연산수r

arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
nums = list(map(int, sys.stdin.readline().strip().split()))
for num in nums:
    n, m = len(arr), len(arr[0])
    if num == 1:
        temp = [[0]*m for _ in range(n)]
        idx = -1
        for j in arr:
            temp[idx] = j
            idx-=1
            
    elif num == 2:
        temp = [[0]*m for _ in range(n)]
        for idx, val in enumerate(arr):
            temp[idx] = list(reversed(val))
            
    elif num == 3:
        temp = [[0]*n for _ in range(m)]
        x,y = 0,-1
        for j in arr:
            for val in j:
                temp[x][y] = val
                x+=1
            x=0
            y-=1
            
    elif num == 4:
        temp = [[0]*n for _ in range(m)]
        x,y = -1,0
        for j in arr:
            for val in j:
                temp[x][y] = val
                x-=1
            x=-1
            y+=1
            
    elif num == 5:
        temp = [[0]*m for _ in range(n)]
        
        for x in range(n//2): # 1->2
            for y in range(m//2):
                temp[x][m//2 +y] = arr[x][y]
                
        for x in range(n//2): # 2->3
            for y in range(m//2, m):
                temp[(n//2)+x][y] = arr[x][y]
        
        for x in range(n//2, n): # 3->4
            for y in range(m//2, m):
                temp[x][y-(m//2)] = arr[x][y]
                
        for x in range(n//2, n): # 4->1
            for y in range(m//2):
                temp[x-(n//2)][y] = arr[x][y]
        
    else: # 6    
        temp = [[0]*m for _ in range(n)]
        for x in range(n//2): # 1->4
            for y in range(m//2):
                temp[x+(n//2)][y] = arr[x][y]
                
        for x in range(n//2): # 2->1
            for y in range(m//2, m):
                temp[x][y-(m//2)] = arr[x][y]
        
        for x in range(n//2, n): # 3->2
            for y in range(m//2, m):
                temp[x-(n//2)][y] = arr[x][y]
                
        for x in range(n//2, n): # 4->3
            for y in range(m//2):
                temp[x][y+(m//2)] = arr[x][y]
    arr = temp.copy()

for i in arr:
    print(*i)