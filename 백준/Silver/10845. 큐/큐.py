import sys

n = int(sys.stdin.readline().strip())

que = []
for _ in range(n):
    command = str(sys.stdin.readline().strip())
    p = ""
    if command.startswith("push"):
        que.append(int(command.split()[1]))
    else:
        if command == 'pop':
            if len(que)==0:
                p = -1
            else:
                p = que.pop(0)
        elif command == 'size':
            p = len(que)
        elif command == 'empty':
            if len(que)==0: p=1
            else: p=0
        elif command == 'front':
            if len(que)==0:
                p = -1
            else: p=que[0]
        elif command == 'back':
            if len(que)==0:
                p = -1
            else: p=que[-1]
        print(p)