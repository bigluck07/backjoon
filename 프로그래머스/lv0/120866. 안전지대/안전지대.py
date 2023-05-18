def solution(board):
    answer = 0
    ch = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
    xy = len(board)
    visited = [[0]*xy for _ in range(xy)]
    for y,ls in enumerate(board):
        for x,val in enumerate(ls):
            if val == 1:
                for dx,dy in ch:
                    if 0<=x+dx<xy and 0<=y+dy<xy: 
                            visited[y+dy][x+dx] = 1
    
    for i in visited:
        print(i)
        for j in i:
            if j == 0:
                answer+=1
    return answer