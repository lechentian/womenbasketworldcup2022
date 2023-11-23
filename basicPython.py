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

print("==================== indentation")

if True:
    print("Answer")
    print("True")
else:
    print("Answer")
print ("False")# 缩进不一致，会导致运行错误

print("==================== variable")
x = 10
x = x + 2

print(x)
print(type(x))

x = "I am X"
print(x)
print(type(x))


a = 'ABC'
b = a
a = 'XYZ'
print(b)
print(type(b))

print("==================== variable type")
'''
Number（数字）
String（字符串）
bool（布尔类型）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）

'''


print("====================number")
counter = 100 # 整型变量
miles =1000.0# 浮点型变量
name = "runoob"  # 字符串

print(counter)
print(miles)
print(name)

print(5 + 4)
print(4.3 - 2)
print(3 * 7 )

print(2 / 4)
#0.5
print(2 // 4) # 除法，得到一个整数
#0
print(17 % 3) # 取余
#2
print(2 ** 5) # 乘方
#32

print("====================string")
str = 'Runoob'

print(str)# 输出字符串
print(str[0:-1])# 输出第一个到倒数第二个的所有字符
print(str[0])# 输出字符串第一个字符
print(str[2:5]) # 输出从第三个开始到第五个的字符
print(str[2:])# 输出从第三个开始的后的所有字符
print(str * 2) # 输出字符串两次，也可以写成 print (2 * str)
print(str + "TEST") # 连接字符串


print("====================bool")
a = True
b = False

# 比较运算符
print(2 < 3) # True
print(2 == 3) # False

# 逻辑运算符
print(a and b)# False
print(a or b) # True
print(not a) # False

# 类型转换
print(int(a)) # 1
print(float(b)) # 0.0
#print(str(a)) # "True"


print("====================list")

a = [1, 2, 3, 4, 5, 6]
#print(a[0]) = 9
a[2:5] = [13, 14, 15]
print(a)
#[9, 2, 13, 14, 15, 6]
a[2:5] = []  # 将对应的元素值设置为 []
print(a)
#[9, 2, 6]

print("====================tuple")
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print (tuple)  # 输出完整元组
print (tuple[0])
print (tuple[1:3]) # 输出从第二个元素开始到第三个元素
print (tuple[2:])  # 输出从第三个元素开始的所有元素
print (tinytuple * 2)  # 输出两次元组
print (tuple + tinytuple) # 连接元组


print("====================dict")
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]  = "2 - 菜鸟工具"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}

print (dict['one'])  # 输出键为 'one' 的值
print (dict[2])  # 输出键为 2 的值
print (tinydict) # 输出完整的字典
print (tinydict.keys())  # 输出所有键
print (tinydict.values()) # 输出所有值

print("====================if")
age = 2
if age <= 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)


print("====================for")
sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    print(site)

print("====================function")
def max(a, b):
    if a > b:
        return a
    else:
        return b

a = 4
b = 5
print(max(a, b))


print("====================json")
import json
with open('women_basket_world_cup_2022_all_players.json') as json_file:
    data = json.load(json_file)
for dat in data:
    print(type(dat))
    print(dat)
