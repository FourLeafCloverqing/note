# 1. 面向过程
# 2. 面向对象

# class

# 类
# 入门
# class Person:
#     #  __init__ 构造方法
#     def __init__(self, name, age):
#         # name和age是属性
#         print('创建了一个人')
#         self.name = name
#         self.age = age
#         self.hp = 100
#
#     def battle(self, other):
#         if other.hp < 0:
#             print(f'{other.name}已经死亡, 不要再打了')
#             return
#         other.hp -= 1
#         if other.hp < 0:
#             print(f'{other.name}的hp -1 , 已经死亡, 剩余: {other.hp}')
#         else:
#             print(f'{other.name}的hp -1 , 剩余: {other.hp}')
#
#     def xxx(self):
#         print('不知道干嘛')
#
#
#     def run(self):
#         print('两条腿跑.')
#
#
# class Animal:
#     def run(self):
#         print('四条腿跑.. ')


# 继承, 多继承
# class Singer(Animal, Person):
#     def sing(self, content):
#         print(f'{self.name}  唱道: {content}')
#
#     def battle(self, other):
#         print('歌手也可以打架 ')
#         super(Singer, self).battle(other)
#
#     def __init__(self, name, age, product):
#         super(Singer, self).__init__(name, age)
#         self.product = product


# 人 -> 名字年龄性学校 , 吃饭说话走路

# if __name__ == '__main__':
    # 创建对象(caixukun)
    # caixukun = Singer('蔡徐坤', 12, '鸡你太美')
    # caixukun.sing("我唱了唱了唱了... ")
    # caixukun.run()
    # print(caixukun.age)
    # print(f'{caixukun.name} 的初始化hp值 {caixukun.hp}')
    # wuyifan = Singer('吴亦凡', 21, '大碗宽面')
    # print(f'{wuyifan.name} 的初始化hp值 {wuyifan.hp}')
    #
    # for i in range(103):
    #     caixukun.battle(wuyifan)
# class myclass:
#     def __init__(self):
#         self.data = []
# x = myclass()  #有疑问？？？
# print("myclass的属性为",x)

# class JustCounter:
#     __secretCount = 0  # 私有变量
#     publicCount = 0  # 公开变量
#
#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print(self.__secretCount)


# counter = JustCounter()
# counter.count()
# counter.count()
# print(counter.publicCount)
# print(counter.__secretCount)


###excise  面向对象
#类：用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
#方法：类中定义的函数。
#类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且函数体之外。类变量通常不作为实例变量使用。


#test1：创建一个新的类并将该对象赋给局部变量x，x是空变量,其中类中包含变量和方法
# class myclass:
#     i = "12345"
#     def combination(self):
#         print("including wsq")
#         return "including wsq"
# x = myclass()
# print(x.i,x.combination())
#notes:x是一个空变量


#test2:__init__()方法可以有参数，可以没有参数，有参数时参数通过__init__()传递到类中的实例化操作。
#没有参数
# class people:
#     n = 'wsq'
#     a = 0
#     def person (self):
#         print("我们是好朋友")
#         return 'hello world'
# x = people()
# print(x.a,x.n,x.person())
#有参数，一定要用__init__(self, para_1,para_2,....)，不能用其他的person
# class people:
#     n = 'wsq'
#     a = 0
#     def __init__(self, name, age):
#         self.n = name
#         self.a = age
# x = people('wsf', 26)
# print("her name is %s,she is %d years old" %(x.n,x.a))        #notes:这里输入的数应该是x.n，x.a


#test3:self代表的是实例而不是类，类的方法与普通函数只有一个区别，他们必须有一个额外的第一个参数名称，按照惯例它的名称是self，self不是关键字，换成别的字母也可以
# class person:
#     def myhobby(yourself):
#
#         return 'my hobby is happy'
#     def mydream(self):
#         print('my hobby is happy')
# x = person()
# x.myhobby()

# test4：定义基本属性、私有属性，私有属性在外部无法访问
# class person:
#     age_1 = 0
#     __age_2 = 0
#     def change(self):
#         self.age_1 += 1
#         self.__age_2 +=1
#         print(self.__age_2)
# x = person()
# x.change()
# x.change()     #在调用函数时应该是左侧+，变量名称
# x.change()
# print(x.age_1)
# print(x.__age_2)     #私有属性在外部无法访问
# def people(person):



#单继承实例
#父类函数
# class anamal:
#     n = 'name'
#     a = 'age'
#     def __init__(self,name,age):
#         self.n =name
#         self.a = age
    # def speak(self):
#         print("This is %s,it is %d years old" %(self.n,self.a))
#
# class dog(anamal):
    # x= anamal('haba',2)
    # m = ''

    # def __init__(self, name,age):
    #     super(dog,self).__init__(name,age)
        #单继承，调用父类的函数
        # anamal.__init__(self,name,age)
        # self.m = femal
   #覆写父类的方法
    # def speak(self):
    #     anamal.speak(self)
    #     print('This is %s, the animal is %s' %(self.n,self.m))
    #
    #     print('the animal is %s' %self.m)
#
# x = dog('haba',2)
# x.speak()
# x.__init__('haba',2)


#多继承
# class people:
#     #定义基本属性
#     name = ''
#     age = ''
    #定义私有属性
    # __weight = ''
    #定义构造方法
    # def __init__(self,n,a):
    #     self.name = n
    #     self.age = a
    # def speak(self):
    #     print('her name is %s,she is %d years old'%(self.name,self.age))
    #     # print('her name is %s,she is %d years old'%(n,a))

#单继承实例
# class student:
#     femal = ''
#     def __init__(self,n,a,m):  #在继承时应该有self
      #调用父类函数
      # people.__init__(self,n,a)
      # self.femal = m
    #覆写父类方法
    # def speak(self):
    #     print('her name is %s,she is %s'%(self.name,self.femal))

#另一个类，多继承之前的准备
# class adult:
#     hobby = ''
#     dream = ''
#     def __init__(self,h,d):
#         self.hobby = h
#         self.dream = d
#     def speak(self):
#         print('her bobby is %s,her dream is %s'%(self.hobby,self.dream))
#
# class sample(student,adult):
#     def __init__(self,n,a,m,h,d):
#         student.__init__(self,n,a,m)
#         adult.__init__(self,h,d)
# x = sample('wsf',26, 'foll','money','hapyy')
# x.speak()


# test7：方法重写：super()函数用于调用父类（超类）的一个方法
# class parents:
#     i = '12345'
#     def love(self):
#         print('this is life')
#
# class child:
#     def love(self):
#         # parents.love(self)
#         print('this is dream')
# x = child()
# x.love()
# super(child, x).love()
#test7：Python子类继承父类构造函数说明
# class Parent:  # 定义父类
#     def myMethod(self):
#         print('调用父类方法')
#
#
# class Child(Parent):  # 定义子类
#     def myMethod(self):
#         print('调用子类方法')


# c = Child()  # 子类实例
# c.myMethod()  # 子类调用重写方法
# super(Child, c).myMethod()  # 用子类对象调用父类已被覆盖的方法



# class person:
#     age_1 = 0
#     __age_2 = 0
#     def change(self):
#         self.age_1 += 1
#         self.__age_2 +=1
#         print(self.__age_2)
#     def __change(self):
#         print('i love life')
# x = person()
# x.change()
# x.change()     #在调用函数时应该是左侧+，变量名称
# # x.__change
#
# print(x.age_1)
# print(x.__age_2)     #私有属性在外部无法访问



###练习读写文件
# x = open('test.txt','w')
# content = x.read()
# print(content)
# x.write('abcdefghijklmnopqratuvwwxyz')
# x.close
# x = open('test.txt','a')
# x.write('abcdefghijklmnopqratuvwwxyz111')
#
#
# x = open('test.txt','r')
# content = x.read()
# print(content)
#
# f = open('test.txt', 'r')

#复制粘贴一个文件的内容到另一个文件中
# def copy_file():
#     first_file = open('test.txt','r')
#     content = first_file.read()
#     second_file = open('test_1.txt','w')
#     second_file.write(content)
# x=copy_file()
# print('')


##错误和异常
# while True print('Hello world')
# 10 * (1/0)
# '2'+2

# def hanshu():
#     a = 10
#     try:
#         a <5
#         print('该值小于5')
#     except:
#         print('该值大于等于5')
#     finally:
#         print('该值是一个整数')
# hanshu()


# def this_fails():
#     x = 1 / 0
#
# try:
#     this_fails()
# except ZeroDivisionError:
#     print('division by zero')
##test1:异常处理的第一种方式，try except finally

# this_fails()
# def fail():
#     try:
#         2+2
#         print('字符串和数字可以相加')
#     except TypeError:
#         print('字符串和数字不可以相加')
#     else:
#         print('写这里是无意义的，因为已经知道是错误的')
#     finally:
#         print('我真的理解了')
# fail()

##test2:通过with关键字制定文件对象的上下文环境并将离开上段环境时自动释放文件资源

# def open_file():
#     try:
#         with  open('first.txt') as f:
#             print(f.read())
#     except FileNotFoundError:
#         print('该文件不存在')
#     except LookupError:
#         print('指定了未知的编码!')
#     except UnicodeDecodeError:
#         print('读取文件时解码错误!')
#     finally:
#         print('该文件状况不清楚')
#     #     # if f:
#     #     f.close()
# open_file()

##test3：三种读取文件内容的方式

import time
# def read_file():
    # with open('test.txt') as f:
    #     print(f.read())  #读取整个文件内容
    # with open('test.txt') as f:
    #     for line in f:  #按行读取内容
    #         print(line,end='\t')
    #         time.sleep(0.5)
    # # print()
#     with open('test.txt') as f:
#         line =f.readlines() #读取文件按行读取到列表中
#         print(line)
# read_file()
# f = open('second.txt','w')

##test4:将1-9999之间的素数分别写入三个文件中

# import math
# def sushu(n):
#     assert n > 0
#     if n >= 1:
#         for i in range(2,n-1):
#             if n % i == 0:
#                 return False
#             else:
#                 return True
# def sushu(n):
#     assert n > 0
#     for i in range(2,int(math.sqrt(n))+1):
#         if n == 1:
#             return False
#         elif n >= 2:
#             if n% i == 0:
#                 return False
#             else:
#                 return True
# def write_in_sushufile():
#     x = open('first_1.txt','w')
#     y = open('second_1','w')
#     z = open('third_1.txt','w')
#     for number in range(1,99):
#         l = sushu(number)
#         if l == True:
#             x.write(str(number) +'\n')
#             # print('素数是%d'%number)  ##多出一个1
#     x.close()
#     content_1 =open('first_1.txt','r')
#     content_first = content_1.read()
#     print(content_first)
#     # x.read()
#
#     for number in range(100,999):
#         j = sushu(number)
#         if j == True:
#             y.write(str(number)+'\n')
#     y.close()
#     content_2 = open('second_1','r')
#     content_second = content_2.read()
#     print(content_second)
#     for number in range(1000,999):
#         k = sushu(number)
#         if k == True:
#             z.write(str(number)+'\n')
#     z.close()
#     content_3 = open('third_1.txt','r')
#     content_third = content_3.read()
#     print(content_third)
#
# write_in_sushufile()
# content_1 =
# print(y)
# print(z)
# import math
# def is_prime(n):
#     """判断素数的函数"""
#     assert n > 0
#     for factor in range(2, int(math.sqrt(n)) + 1):
#         if n % factor == 0:
#             return False
#     return True if n != 1 else False
# def see_return(n):
#     l = is_prime(n)
#     if l ==True:
#         print(n)
# see_return(1)


##test5:读写二进制文件
# def read_b():
#     file_1 = open('test.txt','rb')
#     content1 = file_1.read()
#     print(content1)
# read_b()

##test6:读写jump文件
# import json
# def python_to_json():
#     dict1 = {'name' : 'wsf','age':26,'sex':'female','hobby':'funny'}
#     try:
#         with open('wenben.txt','w') as fs:
#             json.dump(dict1,fs)
#             fs.close()
#             l = open('wenben.txt','r')
#             content = l.read()
#             print(content)
#     except IOError as e:
#         print(e)
#     print('保存成功')
# python_to_json()

##test7:让用户输入一个合法的整数，但允许用户中断这个程序
##test8:最后一个except语句可忽略异常的名称，他将被当做通用符使用。
# def int_num():
#     try:
#         number = int(input('请输入一个正整数'))
#         print('输入成功，您输入的的正整数为：')
#     except ValueError:
    # except :
#         print('您输入的非正整数，输入错误，请重新输入')


# def int_num():
#     number = int(input('请输入一个正整数：'))
# int_num()

##test10:以实例如果x>5就触发异常
# def happen():
#     num = int(input('请输入一个数字：'))
#     if num > 5:
#         raise Exception ('num值不可大于5，x值为：%d' %num)
#
# happen()





