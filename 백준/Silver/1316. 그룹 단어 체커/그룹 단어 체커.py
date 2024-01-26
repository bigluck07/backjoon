# 1. 단어 N개 입력
import sys
word_cnt = int(sys.stdin.readline().strip())
answer = 0
for _ in range(0, word_cnt):
    word = str(sys.stdin.readline().strip())
    # 2. 각 단어가 그룹 단어인지 확인
    leters = []
    num = 0
    l = word[0]
    # 3. 단어가 다 반복이면 중지
    if len(word) == word.count(l):
        answer+=1
        word="" 
    # 4. 단어를 줄여가면서 확인하기
    while word:
        # 5. 첫단어가 리스트에 있는지 확인
        if l in leters:
            break
        # 5-1. 마지막까지 연속된다면
        if num == len(word):
            answer+=1
            break
        # 5-2. 연속되는 글자인지 확인
        if word[num] == l:
            num+=1
        # 6. 연속되지 않으면 목록에 넣기
        else:
            leters.append(l)
            word = word[num:]
            # 7-1. 남은 글자 확인 후 없으면 word를 "" 만듬
            if len(word) == 0:
                word = ""
                answer+=1
            else: # 남은글자 존재
                # 5-1. 연속되는 글자 리스트에 넣고, 다음 글자가 이미 들어있었는지 확인
                if len(word) == 1 and word[0] not in leters:
                    answer+=1
                    word = ""
                else:
                    l = word[0]
                    num=1
print(answer)