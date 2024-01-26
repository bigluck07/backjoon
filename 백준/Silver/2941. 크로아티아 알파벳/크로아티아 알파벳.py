leter = ["c=", 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input().strip()
cnt = 0
lnth = len(word)
num = 3
while word:
    if word in leter:
        cnt+=1
        word=""
        continue
    if num == 1:
        if word[0]in leter:
            cnt+=1
        else:
            leter.append(word[0])
            cnt+=1
        if len(word) > 1:
            word = word[1:]
        else:
            word = ""
        num = 3
        continue

    if word[:num] in leter:
        cnt+=1
        word = word[num:]
        num=3
    else:
        num-=1
print(cnt)