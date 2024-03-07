# 1. 입력
import sys
n = int(sys.stdin.readline().strip())
num_ls1 = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
num_ls2 = list(map(int, sys.stdin.readline().strip().split()))

answer = []
plus = []
num_dic = {x:1 for x in set(num_ls1)}

for i in num_ls2:
    try:
        answer.append(num_dic[i])
    except:
        answer.append(0)
print(*answer, sep=' ')