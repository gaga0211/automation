import math

def quadratic(a, b, c):
    x1 = ( -b + math.sqrt((b*b - 4*a*c)) ) / (2*a)
    x2 = (-b - math.sqrt((b*b - 4*a*c))) / (2*a)
    return x1,x2

x1,x2 = quadratic(2,8,4)
print('x1,x2',x1,x2)

#打印从1到100的数字中所有能被3整除，又能被5整除的数字有哪些
for i in range(1,101):
    if (i % 3 == 0 and i % 5 ==0):
        print(i)

#输入一个字符串返回满足以下条件的字符串
#如果字符串长度大于 3，添加 ‘ing’ 到字符串的末尾
# 如果字符串是以 ‘ing’ 结尾，就在末尾添加 ‘ly’
# 如果字符串长度小于 3，返回原字符串
str = input("输入一个字符串:")
if len(str) >= 3:
    if str.endswith('ing'):
        str += 'ly'
    else:
        str += 'ing'
else:
    pass
print(str)
# 判断回文
    
