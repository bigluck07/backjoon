# 1. 입력
import sys
p, k= map(int, sys.stdin.readline().strip().split())

for x in range(2, k+1):
    if p%x == 0:
        if x >= k:
            print("GOOD")
        else:
            print("BAD", str(x))
        break
else:
    print("GOOD")