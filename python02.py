#-*- coding: utf-8 -*-
import math
#python 基础
a = 100
if a >= 0 :
    print(0)
else:
    print(-a)

print('I\'m ok.')
print('I\'m learning\nPython.')
print('\\\n\\')
print('''line1
line2
line3''')

age = 123
if age >= 18:
    print('adult')
else:
    print('teenager')

print('包含中文的str')

print('\u4e2d\u6587')

print(b'ABC'.decode('ascii'))

print('ABC'.encode('ascii'))

print(len('ABC'))

print('Hello,%s'%'world')

print('%02d-%02d' % (3, 1))

print('growth rate: %d %%' % 7)

print('Hello,{0},成绩提升了{1:.1f}%'.format('小明',17.125))

print('%.9f' % 3.14159268)

s1 = 72
s2 = 85
r = (s2 - s1) / s1 * 100
print(r)
print('%.1f %%' % r)

# list
classmates = ['michael','bob','tracy']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[-1])
# 增加
classmates.append('adam')
print(classmates)
# 插入
classmates.insert(2,'jack')
print(classmates)
# 删除
classmates.pop(1)
print(classmates)
# 元素替换
classmates[1] = 'fangjia'
print(classmates)
# 元素的数据类型不同
L = ['jiajia',234,True]
print(L)
# 元素也可以是list
s = ['python','java',['asp','php'],'scheme']
print(s)
print(len(s))

# tuple
classmates = ('michael','bob','tracy')
print(classmates)
t = (1)
print(t)
t = (1,)
print(t)
# “可变的”元素
t = ('a','b',['A','B'])
t[2][0] = 'x'
t[2][1] = 'y'
print(t)
# 练习题
L = [['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

# 条件判断
age = 20
if age >= 18:
    print('your age is',age)
    print('adult')

age = 3
if age >= 18:
    print('your age is',age)
    print('adult')
else:
    print('your age is',age)
    print('teenager')

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# input
s = input('birth:')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

# 练习题
height = 1.75
weight = 100.5
bmi = weight / (height * height)
if bmi < 18.5:
    print('过轻')
elif bmi >=18.5 and bmi < 25:
    print('正常')
elif bmi >=25 and bmi < 28:
    print('过重')
elif bmi >=28 and bmi <32:
    print('肥胖')
else:
    print('严重肥胖')

# 循环
names = ['michael','bob','tracy']
for name in names:
    print(name)

sum = 0 
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)

sum = 0 
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n -2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('Hello,' + name + '!')

n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')

n = 0 
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)

# dict
d = {'michael':95,'bob':76,'tracy':87}
print(d['michael'])

s = set([1, 1, 2, 2, 3, 3])
s.add(4)
print(s)
s.remove(2)
print(s)

d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))

a = 'abc'
b = a.replace('a', 'A')
print(b)

# 函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))

def power(x):
    return x * x

print(power(5))

def power1(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power1(5,2))

std1 = {'name':'michael','score':98}
std2 = {'name':'bob','score':81}

def print_score(std):
    print('%s:%s' % (std['name'], std['score']))

print_score(std1)
print_score(std2)

def MyFunction(name):
    print("this is my first function:%s" %name)

MyFunction("functionName")

def MyFunction2(action,name = "DefaultName"):
    print("this is my first function: %s,the action is: %s" %(name,action))
MyFunction2("action for test")

class Turtle:
    color = 'green'
    weight = 10 
    legs = 4
    shell = True
    mouth = "大嘴"

    def climb(self):
        print("climb")
    
    def run(self):
        self.weight = self.weight - 1
        print("run")

    def bite(self):
        print("bite")

    def eat(self):
        print("eat")

    def sleep(self):
        print("sleep")


print('Turtle()1', Turtle().weight)
print('Turtle()2', Turtle().weight)

t = Turtle()
print('weight', t.weight)
t.run()

class A:
    def fun(self):
        print("我是小A")

class B:
    def fun(self):
        print("我是小B")

a = A()
a.fun()

class Ball:
    def setName(self,name):
        self.name = name
    def kick(self):
        print("啦啦啦啦%s" %self.name)

a = Ball()
a.setName('ll')
b = Ball()
b.setName('ss')
c = Ball()
c.setName('ee')
a.kick()

class Ball1:
    def __init__(self,name):
        self.name = name
    def kick(self):
        print("啦啦啦啦%s" %self.name)

a = Ball1('fangjia')
a.kick()

class Person:
    name = "小甲鱼"

p = Person()
print(p.name)

class Parent:
    def hello(self):
        print("正在调用父类方法")

class Child(Parent):
    def hello(self):
        print("正在调用子类方法")

p = Parent()
p.hello()
c = Child()
c.hello()

import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(1,10)
        self.y = r.randint(1,10)
    
    def move(self):
        self.x -= 1
        print("我的位置是：",self.x,self.y)
    
class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass    

class Shark(Fish):
    def __init__(self):
        super().__init__()
        self.hungry = True
    
    def eat(self):
        if self.hungry:
            print("吃货的梦想")
            self.hungry = False
        else:
            print("太撑了")

fish = Fish()
fish.move()
goldfish = Goldfish()
goldfish.move()
shark = Shark()
shark.eat()
shark.eat()
shark.move()

brand = ['李宁','耐克','阿迪达斯','鱼c工作室']
slogan = ['一切皆有可能','just do it','impossible is nothing','让编程改变世界']
print ('鱼c工作室的口号是：',slogan[brand.index('鱼c工作室')])

dict1 = {'李宁':'一切皆有可能','阿迪达斯':'just do it','阿迪达斯':'impossible is nothing','鱼c工作室':'让编程改变世界'}   
print('鱼c工作室的口号是：',dict1['鱼c工作室'])

d1 = {}
d1.fromkeys((1,2,3),'Number')

import time as t

class MyTimer():
    # 开始计时
    def start(self):
        self.start = t.localtime()
        print("计时开始...")

    # 停止计时
    def stop(self):
        self.stop = t.localtime()
        print("计时结束")

    # 内部方法，计算运行时间
    def _calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for index in range(6):
            self.lasted.append(self.stop[index] - self.start[index])
            self.prompt += str(self.lasted[index])
