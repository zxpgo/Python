score = int(input('请输入你的成绩：'))
if 100 >= score  >= 90:
    print('A')
if 90 > score  >= 80:
    print('A')
if 80 > score  >= 60:
    print('A')
if 0 <= score <60:
    print('D')
if score < 0 or score >100:
    print("输入错误")
