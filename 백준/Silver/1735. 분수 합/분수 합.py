# 1. 입력
import sys
a, b = map(int, sys.stdin.readline().strip().split())
c, d = map(int, sys.stdin.readline().strip().split())

e = (a*d) + (c*b)
f = b*d

big_num = f
small_num = e
while True:
    v = big_num%small_num
    if v == 0:
        break
    else:
        big_num = small_num
        small_num = v

print(e//small_num, f//small_num)