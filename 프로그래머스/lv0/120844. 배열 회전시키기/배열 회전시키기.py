def solution(numbers, direction):
    numbers = list(numbers)
    if direction == 'right':
        temp = numbers.pop()
        numbers = [temp]+numbers
    else:
        temp = numbers[0]
        numbers = numbers[1:]+[temp]
        

    return numbers