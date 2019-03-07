file_name = input("请输入你想打开的文件：")

f =  open(file_name)
print('文件的内容是：')
for each_line in f:
    print(each_line)
