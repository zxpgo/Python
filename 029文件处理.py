f = open("F:\\record.txt")
boy = []
girl = []
count = 1;

for each_line in f:
    if each_line[:6] != '======':
        #进行字符串分割
        (role, line_spoken) = each_line.split(':',1)
        if role == 'zxp':
            boy.append(line_spoken)
        else:
            girl.append(line_spoken)

    else:
        #分别对文件进行保存
        file_name_boy = 'boy_' + str(count) + '.txt'
        file_name_girl = 'girl_' + str(count) + '.txt'

        boy_file = open(file_name_boy, 'w')
        girl_file = open(file_name_girl, 'w')

        boy_file.writelines(boy)
        girl_file.writelines(girl)

        boy_file.close()
        girl_file.close()

        boy = []
        girl = []
        count += 1

file_name_boy = 'boy_' + str(count) + '.txt'
file_name_girl = 'girl_' + str(count) + '.txt'

boy_file = open(file_name_boy, 'w')
girl_file = open(file_name_girl, 'w')

boy_file.writelines(boy)
girl_file.writelines(girl)

boy_file.close()
girl_file.close()
f.close()
