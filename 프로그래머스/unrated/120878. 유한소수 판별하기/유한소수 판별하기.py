def solution(a, b):
    
    import math
    c = b//math.gcd(a,b)
    
    while True:
        if c%2: break
        c = c//2
    while True:
        if c%5: break
        c = c//5

    return 1 if c==1 else 2
