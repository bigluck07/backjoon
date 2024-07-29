def solution(friends, gifts):
    # answer = 0
    
    name_list = {}
    for i in friends:
        name_list[i] = {'gisu':0}
        for j in friends:
            if i == j:
                continue
            name_list[i][j]=0

    
    for i in gifts:
        a,b = i.split()
        
        name_list[a]['gisu'] += 1
        name_list[b]['gisu'] -= 1
        name_list[b][a]+=1
        
    #print(name_list)
    
    gift_num = {i:0 for i in friends}
    temp = []
    for i in friends:
        temp.append(i)
        for j in name_list[i]:
            if (i == j) | (j=='gisu') | (j in temp):
                continue
            else:
                # 선물수가 같다면
                if name_list[i][j] == name_list[j][i]:
                    # 지수가 같다면
                    if name_list[i]['gisu'] == name_list[j]['gisu']:
                        continue
                    elif name_list[i]['gisu'] > name_list[j]['gisu']:
                        gift_num[i]+=1
                    else:
                        gift_num[j]+=1
                else:
                    if name_list[i][j] > name_list[j][i]:
                        gift_num[j]+=1
                    else:
                        gift_num[i]+=1

    return max(gift_num.values())



'''
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
def solution(friends, gifts):
    f = {v: i for i, v in enumerate(friends)}
    l = len(friends)
    p = [0] * l
    answer = [0] * l
    gr = [[0] * l for i in range(l)]
    for i in gifts:
        a, b = i.split()
        gr[f[a]][f[b]] += 1
    for i in range(l):
        p[i] = sum(gr[i]) - sum([k[i] for k in gr])

    for i in range(l):
        for j in range(l):
            if gr[i][j] > gr[j][i]:
                answer[i] += 1
            elif gr[i][j] == gr[j][i]:
                if p[i] > p[j]:
                    answer[i] += 1
    return max(answer)
'''