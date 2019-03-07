def discounts(price, rate):
    final_price = price * rate
    print("访问全局变量old_price的值：", old_price)
    old_price = 50#与全局变量old_price存储在不同的空间
    print("修改后old_price的值为：", old_price)
    return final_price

old_price = float(input("请输入原价："))
rate = float(input("请输入折扣："))
new_price = discounts(old_price, rate)
print("打折以后价格为：", new_price)
print("修改后old_price的值为：", old_price)
print("这里试图打印局部变量final_price的值：", final_price)
#final属于局部变量，old_price，rate是全局变量
