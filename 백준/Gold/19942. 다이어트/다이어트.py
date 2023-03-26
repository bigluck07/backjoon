import sys
from itertools import combinations
n = int(sys.stdin.readline().strip())
minimum_list = list(map(int, sys.stdin.readline().strip().split()))
food_list = [[]]

for i in range(n):
    food_list.append(list(map(int, sys.stdin.readline().strip().split())))

res = []
cost = 999999999999

for i in range(1, n+1):
    for combo in combinations(range(1, n+1), i):
        # check_costNnimum(combo)
        p, f, s, v, c = 0,0,0,0,0
        for num in combo:
            p+=food_list[num][0] 
            f+=food_list[num][1]
            s+=food_list[num][2]
            v+=food_list[num][3]
            c+=food_list[num][4]

        if minimum_list[0] <= p and minimum_list[1]<=f and minimum_list[2]<=s and minimum_list[3]<=v:
            if c < cost:
                cost = c
                res = combo
            elif c == cost:
                res = sorted((res, combo))[0]

if cost == 999999999999:
    print(-1)
else:
    print(cost)
    print(*res)