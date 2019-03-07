def hanoi(n,x,y,z):
    if n==1:
        print(x,"-->",z)
    else:
        hanoi(n-1,x,z,y)#将前n-1个盘子从x移动到y
        print(x,"-->",z)
        hanoi(n-1,y,x,z)

n=int(input("请输入汉鲁塔层数："))
hanoi(n,'x','y','z')
