# 1. 입력 받기 과목명, 학점, 성적 - 20 과목
import sys
class_grd_total, class_pnt_total = 0, 0
grd2num = {'A+':4.5, 'A0':4.0,
           'B+':3.5, 'B0':3.0,
           'C+':2.5, 'C0':2.0,
           'D+':1.5, 'D0':1.0, 'F':0.0}

for _ in range(20):
    sbj, pnt, grd = sys.stdin.readline().strip().split()
    # 2. 패논패를 제외한 과목별합 구하기
    if grd != 'P':
        class_pnt_total+=float(pnt)
        class_grd_total+=(float(pnt)*grd2num[grd])
if class_pnt_total == 0:
    print(0.000000)
else:
    print(class_grd_total/class_pnt_total)