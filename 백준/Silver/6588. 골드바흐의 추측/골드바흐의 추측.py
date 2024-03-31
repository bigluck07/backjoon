import sys
input = sys.stdin.readline
print = sys.stdout.write
MAX = 1000001

def solve():
    # 에라토스테네스의 체
    sieve = [False]*2 + [True]*(MAX-2)
    for i in range(3,int(MAX**0.5),2):
        if sieve[i]:
            sieve[i*2::i] = [False]*((MAX-i-1)//i)

    # 소수 리스트 구하기
    prime = []
    for i in range(3,MAX,2):
        if sieve[i]:
            prime.append(i)

    # 추측 검증
    while True:
        n = int(input())
        if not n:
            break

        for i in prime:
            if sieve[n-i]:
                print("%d = %d + %d\n" %(n,i,n-i))
                break
solve()