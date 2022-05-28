f = int(input("请输入华氏温度："))
c = (f - 32) / 1.8

# 关于字符串的格式化输出：
# https://www.runoob.com/python/att-string-format.html
print("{:.1f}华氏温度={:.1f}摄氏温度".format(f, c))
