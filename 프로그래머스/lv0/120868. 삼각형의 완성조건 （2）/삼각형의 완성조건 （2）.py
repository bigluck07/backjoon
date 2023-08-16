def solution(sides):
    answer = []
    sides.sort()
    num1 = sides[0]
    num2 = sides[1]
    for i in range(1, num2):
        if i+num1 > num2:
            answer.append(i)
        if i > num2:
            break
    num3 = num1+num2
    while num2 < num3:
        answer.append(num2)
        num2+=1
    answer = set(answer)
    return len(answer)