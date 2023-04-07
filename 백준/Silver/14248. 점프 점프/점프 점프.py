import sys
from collections import deque

n = int(sys.stdin.readline().strip())
A_ls = [0]+list(map(int, sys.stdin.readline().strip().split()))
s = int(sys.stdin.readline().strip())
visited = [0 for _ in range(len(A_ls))]
visited[s] = 1
hp = deque([s]) # 위치

while hp:
    idx = hp.popleft()
    point = A_ls[idx]
    left = idx-point
    right = idx+point
    if  0 < left < len(A_ls): # 돌다리밖 체크
        if visited[left] == 0:
            visited[left]=1
            hp.append(left)
    if  0 < right < len(A_ls): # 돌다리밖 체크
        if visited[right] == 0:
            visited[right]=1
            hp.append(right)
            
print(sum(visited))