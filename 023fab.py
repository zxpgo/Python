def fab(n):
    n1 = 1
    n2 = 1
    n3 = 1

    if n < 0:
        print("输入有误！")
        return -1
    
    while (n-2) > 0:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        n -= 1
    return n3


num = int(input("请输入月份数："))
total = fab(num)
if total != -1:
    print('兔子总数为：%d' % total)
