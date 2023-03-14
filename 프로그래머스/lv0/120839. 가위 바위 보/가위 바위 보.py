def solution(rsp): # 가2 바0 보5
    answer = ''
    for i in rsp:
        if i == "0":
            answer+="5"
        elif i == "2":
            answer+="0"
        else:
            answer+="2"
    return answer