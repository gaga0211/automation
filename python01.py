import math

# def quadratic(a, b, c):
#     x1 = ( -b + math.sqrt((b*b - 4*a*c)) ) / (2*a)
#     x2 = (-b - math.sqrt((b*b - 4*a*c))) / (2*a)
#     return x1,x2

# x1,x2 = quadratic(2,8,4)
# print('x1,x2',x1,x2)

# #打印从1到100数字中所有能被3整除，又能被5整除的数字有哪些
# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)

#输入一个字符串返回满足以下条件的字符串
#如果字符串长度大于 3，添加 ‘ing’ 到字符串的末尾
# 如果字符串是以 ‘ing’ 结尾，就在末尾添加 ‘ly’
# 如果字符串长度小于 3，返回原字符串
# str = input("请输入字符串：")
# if len(str) >= 3:
#     if str.endswith('ing'):
#         str += 'ly'
#     else:
#         str += 'ing'
# else:
#     pass
# print(str)


# 判断回文 回文：62426 为回文数字
# s = input("请输入：")
# a = reversed(list(s))
# if list(a) == list(s):
#     print("yes")
# else:
#     print("no")

# # 定义函数
# def changeme(mylist):
#     mylist.append([1,2,3,4])
#     print("函数内取值：",mylist)
#     return
# # 调用函数
# mylist = [10,20,30]
# changeme(mylist)
# print ("函数外取值：",mylist)

# 可写函数说明
# def printinfo(arg1,*vartuple):
#     print("输出：")
#     print (arg1)
#     for var in vartuple:
#         print (var)
#     return
# # 调用printinfo 函数
# printinfo(10)
# printinfo(70,60,80,79)

# 可写函数说明
# sum = lambda arg1, arg2: arg1 * arg2
# # 调用函数
# print("相乘后的值为：", sum(12,23))
# print("相乘后的值为：", sum(12,34))

# t = 0
# def sum1(a1,a2):
#     t = a1 +a2
#     print("函数内是局部变量：", t)
#     return t
# sum1(12,34)
# print("外的值：", t)

# def power(x):
#     return x * x

# a = 107
# b = power(a)
# print(b)

# c = power(234)
# print(c)

#x^2
def power(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
a = power(8,2)
print(a)