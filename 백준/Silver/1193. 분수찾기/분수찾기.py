import sys
x = int(sys.stdin.readline().strip())#.split())

num = 1

while x > num:
    x-=num
    num+=1

if num % 2 == 0:
    a = x
    b = num-x+1
else:
    a = num-x+1
    b = x
    
print(a, "/", b, sep = "")