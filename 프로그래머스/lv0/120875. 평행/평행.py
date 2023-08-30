from itertools import combinations
def gradient(a,b):
    return (a[1] -b[1])/(a[0]-b[0])

def solution(dots):
    temp = set()
    for d1, d2, d3, d4 in combinations(dots, 4):
        if gradient(d3, d1) == gradient(d2, d4):
            return 1
        if gradient(d4, d3) == gradient(d2, d1):
            return 1
    return 0