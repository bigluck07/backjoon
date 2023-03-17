
import sys
c = int(sys.stdin.readline().strip())


def check_state(idx, sum_state):
    global max_state
    if idx == 11: # 선수 11명 다 확인
        if sum_state>max_state: # 현재 명단의 합과 현재까지 최대능력치합의 비교
            max_state = sum_state
        return
    for x in range(11): # 11케이스
        if player_board[x]: continue # 선발자리 확인
        elif player[idx][x]: # 능력치확인
            player_board[x] = 1
            check_state(idx+1, sum_state+player[idx][x]) #
            player_board[x] = 0 # 재귀돌고 오면 0으로 바꿔서 확인하도록 함
            
            
for _ in range(c): # 테스트케이스 수만큰 반복
    player_board = [0]*11 # 선발선수 능력치
    max_state = 0 # 합계
    player = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(11)] # 선수능력치
    check_state(0,0)
    
    print(max_state)