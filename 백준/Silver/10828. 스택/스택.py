import sys

n = int(sys.stdin.readline().strip())

stck = []
for _ in range(n):
    command = str(sys.stdin.readline().strip())
    p = ""
    if command.startswith("push"):
        stck.append(int(command.split()[1]))
    else:
        if command == 'pop':
            if len(stck)==0:
                p = -1
            else:
                p = stck.pop()
        elif command == 'size':
            p = len(stck)
        elif command == 'empty':
            if len(stck)==0: p=1
            else: p=0
        elif command == 'top':
            if len(stck)==0:
                p = -1
            else: p=stck[-1]
        print(p)