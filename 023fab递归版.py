def fab(n):
    if n < 1:
        print("输入有误！")
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fab(n-1) + fab(n-2)

num = int(input("请输入月份数："))
total = fab(num)
if total != -1:
    print('兔子总数为：%d' % total)
