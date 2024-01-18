import sys
string = input().upper()#sys.stdin.readline().upper()
unique_str = set([i for i in string])
str_dict = {}

for i in unique_str:
  str_dict[i]=string.count(i)

res = sorted(str_dict.items(), key=lambda x : x[1], reverse=True)

if len(res) == 1:
  print(res[0][0])
elif res[0][1] == res[1][1]:
  print('?')
else:
  print(res[0][0])