def solution(my_string):
    answer = 0
    ls = ['1', '2','3','4','5','6','7','8','9','0']
    num = '0'
    for idx, val in enumerate(my_string):
        if val in ls:
            num+=val
            print(num)
        else:
            answer+=int(num)
            num = '0'
        if num !='0' and idx ==len(my_string)-1:
            answer+=int(num)
    return answer