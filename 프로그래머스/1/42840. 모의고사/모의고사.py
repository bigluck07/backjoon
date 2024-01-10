def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt_a, cnt_b, cnt_c = 0,0,0
    
    for i in range(len(answers)):
        if answers[i] == a[i%5]: 
            cnt_a+=1
        if answers[i] == b[i%8]: 
            cnt_b+=1
        if answers[i] == c[i%10]: 
            cnt_c+=1

    max_n = max(cnt_a, cnt_b, cnt_c)
    res = []
    if cnt_a == max_n:
        res.append(1)
    if cnt_b == max_n:
        res.append(2)
    if cnt_c == max_n:
        res.append(3)
    return res