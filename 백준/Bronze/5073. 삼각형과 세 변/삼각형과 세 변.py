import sys

while True:
    a, b, c = map(int, sys.stdin.readline().strip().split())

    if (a==b==c==0):
        break
    if (max(a,b,c) >= (a+b+c-max(a,b,c))):
            answer = 'Invalid'
    elif (a==b==c):
        answer = 'Equilateral'
    elif (a==b or a==c or b==c):
        answer = 'Isosceles'
    else:
        answer = 'Scalene'
    print(answer)