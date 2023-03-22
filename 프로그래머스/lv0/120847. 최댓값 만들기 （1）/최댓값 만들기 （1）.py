def solution(numbers):
    answer = 0
    arr = sorted(numbers)
    return arr[-1] * arr[-2]