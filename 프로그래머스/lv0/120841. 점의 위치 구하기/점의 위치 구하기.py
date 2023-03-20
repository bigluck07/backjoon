def solution(dot):
    answer = 0
    x,y = True,True
    
    if dot[0] > 0:
        pass
    else:
        x = False
    if dot[1] > 0:
        pass
    else:
        y = False
    
    if x and y:
        answer = 1
    elif (not x) and y:
        answer = 2
    elif (not x) and (not y):
        answer = 3
    else:
        answer = 4
        
    return answer