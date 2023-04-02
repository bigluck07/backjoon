import sys

words = [str(sys.stdin.readline().strip()) for _ in range(int(sys.stdin.readline().strip()))] # n*m, 연산수r
def permut(l, s):
    global visited, alp
    if l == 0:
        visited.add(s)
        return
    
    for i in range(26):
        if alp[i] > 0:
            alp[i]-=1
            permut(l-1, s+chr(i+97))
            alp[i]+=1

for word in words:
    visited = set()
    alp = [0 for _ in range(26)]
    for x in word:
        alp[ord(x)-97]+=1
    permut(len(word), '')
    
    print(*sorted(list(visited)), sep='\n')