import sys, copy

arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(5)]
nums = [0]
score = {'X':[0,0,0,0,0], 'Y':[0,0,0,0,0], 'C':[0,0]}
hist = arr.copy()
cnt = 0
state = False
for i in range(5):
    nums+=list(map(int, sys.stdin.readline().strip().split()))

for ans, num in enumerate(nums):
    for ix in range(5):
        for iy in range(5):
            if arr[ix][iy] == num:
                score['X'][ix]+=1
                score['Y'][iy]+=1
                if (ix,iy) in [(0,0), (1,1), (2,2),(3,3),(4,4)]:
                    score['C'][0]+=1
                if (ix,iy) in [(0,4),(1,3),(2,2),(3,1),(4,0)]:
                    score['C'][1]+=1
                break
        for i in score.keys():
            for idx, s in enumerate(score[i]):
                if s == 5:
                    cnt+=1
                    score[i][idx] = -5
                if cnt>=3:
                    print(ans)
                    state = True
                if state:
                    break
            if state:
                break
        if state:
            break
    if state:
        break