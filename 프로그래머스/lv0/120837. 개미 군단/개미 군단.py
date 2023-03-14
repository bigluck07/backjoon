def solution(hp): # g5, c3, s1
    
    answer = hp//5 + (hp%5)//3 + (hp%5)%3
    return answer