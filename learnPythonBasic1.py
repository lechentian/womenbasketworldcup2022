# !/usr/bin/python3

# 第一个注释
print("Hello, Python!")
# 第二个注释

'''
第三注释
第四注释
'''

"""
第五注释
第六注释
"""
print("Hello, Python 2!")
print("====================")

if True:
    print("Answer")
    print("True")
else:
    print("Answer")
print ("False")# 缩进不一致，会导致运行错误


print("====================number")
counter = 100 # 整型变量
miles =1000.0# 浮点型变量
name = "runoob"  # 字符串

print(counter)
print(miles)
print(name)


print("====================string")
str = 'Runoob'

print(str)# 输出字符串
print(str[0:-1])# 输出第一个到倒数第二个的所有字符
print(str[0])# 输出字符串第一个字符
print(str[2:5]) # 输出从第三个开始到第五个的字符
print(str[2:])# 输出从第三个开始的后的所有字符
print(str * 2) # 输出字符串两次，也可以写成 print (2 * str)
print(str + "TEST") # 连接字符串
