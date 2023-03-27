def solution(sides):
    answer = 2
    sides.sort()
    if sides[2] < sum(sides[:2]):
        answer=1
    
    return answer