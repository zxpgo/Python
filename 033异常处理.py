try:
    #int('abc')
    
    f = open('我问什么是一个文件.txt','w')
    print(f.write('我存在了'))
    sum = 1 + '1'
    f.close()
except OSError as reason:
    print('文件出错了，错误的原因是：' + str(reason))


except TypeError as reason:
    print('类型出错了，错误的原因是：' + str(reason))

# except (OSError, TyperError):
#     print('类型出错了')
#except :
#    print('出错了')


finally:
    f.close()
    

