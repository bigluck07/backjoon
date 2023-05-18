def solution(polynomial):
    polynomial_sp = polynomial.split(' + ')
    x, num = 0, 0
    for i in polynomial_sp:
        if 'x' in i:
            if i == 'x':
                x+=1
            else:
                x+=int(i[:-1])
        else:
            num+=int(i)
    if x == 1:
        if num != 0 and x != 0:
            answer = f"x + {num}"
        elif num == 0 and x != 0:
            answer = f"x"
    else:
        if num != 0 and x != 0:
            answer = f"{x}x + {num}"
        elif num == 0 and x != 0:
            answer = f"{x}x"
        elif x == 0 and num != 0:
            answer = f"{num}"
        
    return answer