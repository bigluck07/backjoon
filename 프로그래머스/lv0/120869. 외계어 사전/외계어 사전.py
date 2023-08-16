def solution(spell, dic): 
            # 알파벳배열, 외계어배열
    answer = 0
    for i in dic:
        for j in spell:
            state = False
            if j in i:
                state = True
            else:
                break
        if state == True:
            answer = 1
            return answer
    
    answer = 2      
    return answer