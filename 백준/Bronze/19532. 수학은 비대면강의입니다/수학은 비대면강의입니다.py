# 1. 입력
import sys
a, b, c, d, e, f = map(int, sys.stdin.readline().strip().split())

flag = 0
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if (a*x)+(b*y) == c and (d*x)+(e*y)==f:
            print(x,y)
            flag = 1
            break
    if flag == 1:
        break