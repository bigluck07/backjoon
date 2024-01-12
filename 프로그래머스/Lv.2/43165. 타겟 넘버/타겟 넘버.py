def solution(numbers, target):
    
    def calc(x, y):
        nonlocal answer
            
        if x == len(numbers):
            if y == target:
                answer+=1
            return
        
        calc(x+1, y+numbers[x])
        calc(x+1, y-numbers[x])
    answer = 0
    calc(0, 0)
    return answer