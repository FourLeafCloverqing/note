# int
# a = 1
# float
# a = 1.2
# string
# a = 'hello world'

# list: 可以更改的一串值(有顺序)
# a = [1, 2, 3, 5]
## for , append, remove, insert, ...
# tuple: 不可以更改的一串值(有顺序)
# a = (1, 2, 3, 3)
## for, 没有 append, remove, insert
# dict: 键值(没有顺序)
# a = {
#     'age': 18,
#     "name": "Bob",
#     'address': 'DongBei',
#     'fdjslfj': 1,
#     'gender': 'female',
#     'oth': {
#
#     }
# }
# set: 集合, 一些不重复的数,(没有顺序)
## add, remove, for
# a = {1, 3, 5, 6, 67, 7 , 7, 7, 3 }
# b = {1, 5, 3, 6, 67, 7}


#excise
# a = [1, 2, 3, 4, 5]
# print (a)
# a.append(6)#只能这样写,b=a.append(6)写就不对


# b = a
# print (b)
# a.remove(3)
# for i in range(7):#注意是range
#
#     print(a[i])
# num = (1, 2, 3, 4, 5)
# for i in range (5):
#     print(num[i])#注意在此用的也是方括号




# 2020-2-10-excise
# a = 5
# print (a)
#
# b= 1.2
# print(b)
#
# c = 'hello world'
# print(c)'''字典中相关内容

# dictionary = {'name':'shiqingwang', 'age' : 18, 'sex' :'female'}
# seq = ('Google', 'Runoob', 'Taobao')
# dict = dict.fromkeys(seq) # dictionary创建一个新字典？
# print("新字典为 : %s" % str(dict))
# dict = {'Name': 'Zara', 'Age': 7}
# print("Value : %s" %  dict.has_key('Age')) #Python3现在没有这种说法了。
# dictionary1 = {'name':'shifanwang','age':26,'hobby':'money'}
# print(dictionary1.get('dream')) #返回指定键的值,如果值不在字典中，则返回none？
# print(dictionary1.has_key('name'))#如果键在字典中，返回true，否则返回false？Python3现在没有这种说法了。
# print(dictionary.values()) #以列表的形式返回键的值
# print(dictionary.popitem())#以列表的形式返回并删除字典中的最后一对键和值？
# print(dictionary.pop('sex'))#删除字典中给定的键key所对应的值，返回值为被删除的值?
# print(dictionary.fromkeys('hobby','funny'))
# print(dictionary.update(dictionary1))# 将dictionary1中的值更新到dictionary中,用的是update语句？
# print(dictionary1.setdefault('dream')) #与get（）相似，如果键不存在字典中，会添加键并将键值设为default?
# print(dictionary1)
# print(dictionary1.keys())#以列表返回一个字典所有的键
# co(dictionary,dictionary1)  比较两个字典中的
# print(len(dictionary1))  #获取字典中键值的个数
# print(str(dictionary1))#这个还不懂？
# print(type(dictionary1))  #说明类型是字符串、字典、数字等。
# print(dictionary.keys())
# print(dictionary['sex'])  #访问字典里的某个键的值
# dictionary['age'] = 25  #修改字典里的键值，
# dictionary['dream'] = 'happy and money'  #在字典里增加新的键值对
# print(dictionary.items())  #以列表返回可遍历的元组数组
# dictionary.pop('age') #删除字典中的键值对
# dictionary.clear() #删除字典中的所有元素
# dictionary.copy() #返回字典中的一个浅复制
# print(dictionary)
#字典键的特性为：
#1）字典中的键名不可重复，若重复则后面的键值将取代前面的键值
#2）字典中的键类型只能是字符串、数组、数字，不可为列表等
# del dictionary
# print("age对应的键值为",dictionary['age'])
# print(dictionary)
# print("字典中的索引值为：", dictionary.values())


'''

列表中相关内容

# list1 = [1,2,8,3,5]
# list1.sort() #对list进行排序
# print(list1)
# # list1.clear() #清空列表
# list2 = list1.copy()
# print(list2)
# list2 = ['apple','banana','lemon','orange']
# print(list2[2]) #输出列表中的某一位置上的某一值
# print(len(list2))   #脚本操作中的长度描述
# print(max(list1)) #输出list中的最大值
# print(min(list1))
# list3 = ['dog','mouse','pig','chicken']
# list_4 = ['cat','fish']
#
# list3.extend(list_4) #在list中一次性多加几个值
# print(list3)
# b = list3.index('cat')
# print(b)
# list4 = list3.pop(1)
# print("删除的项为：", list4)

# print(list3)
# list4 = [list2,list3]  #list中的嵌套描述
# print(list4)
# list5 = list3 *3 + list2 #list中的组合元素
# print(list5)
# print(list3*3)  #list中的重复
# b = list5.count('dog') #list中某一元素出现的次数
# print(b)
# suq = 'dog' in list3 #list中是否存在某一元素
# print(suq)
# del list5[2] #删除list中的某一位置的元素
# print(list5)
# list中的迭代
# print(list3[0:3])
# print(list3[-2]) #list中的截取
# list3 +=list2  #list中的拼接
# print(list3)

# a = ('apple', 'banana','orange')
# b = list(a)  #将元祖转换为列表
# print(b)

#list中的
# print(list1)
# list1.append(1)
# print(list1)
# list1.remove(2) #移除列表中的某一元素
# print(list1)
# for i in range(4):
#     print(list1 [i])
#     # print(list1[4,1]) 将列表中的数字逆序排列。
# list1.reverse() #反向列表中的元素
# print(list1)
# print(list1[: : -1])
# list1.insert(2,6)
# print(list1)
'''


'''
元祖中相关内容

#元祖的操作和列表基本一致,包括连接+、复制*、截取、元素是否存在、最大最小值的获取、长度
# tuple1 = (1, 2, 5, 7, 9) #tuple (元祖中只有for，无append、insert、remove)
# print(tuple1)
# for i in range (5):
#     print(tuple1[i])
'''

'''
集合中相关内容

# 集合中主要操作包括 add update remove pop discard 判断某一元素是否在集合中  清空集合  计算集合中元素个数  集合之间的与或非
# set1 = {1,2,3,2,4,3,5,6}
# set2 = {1,2,11,13,14,15}
# set3 = set1 | set2
# print(set3)
# set4 = set2 ^set1 #不同时包含在两个元素中
# set4 = set2 & set1
# set4 = set2 - set1
# print(set4)
# set1.remove(1) #移除集合中的某一位置上的元素
# set1.discard(6)
# print(set1)
# set2 = set1.pop()#随机移除集合中的一个元素
# print(set2)
# set1.add(6)
# print(set1)
# set1.update('1')
# print(set1)
# print(set1)
# set1.add(1)
# print(set1)
# for i in range(6):
#     print(set1 [i])
'''


'''条件语句

# a = int(input("请输入整数值："))
# a = 70
# if a < 50:
#     print("该值小于50")
# elif 50 <= a <= 100:
#     print("该值介于50-100之间")
# else:
#     print("该值大于100")

# num1 = int(input("请输入数字"))
# for i in range(1,11):
#     if i == 8:
#         continue
#     else:
#         print(i)
#         # break

# for i in range(1,20):
#     if i % 2 == 0:
#         print("1-20之间的偶数为：", i)
#     else:
#         print("1-20之间的奇数为：", i)

# a = 1
# while a > 0:
#     a += 1
#     if a % 2 == 0 :
#         continue
#     else:
#         print("偶数有：", a)
# a = 0
# while a < 20:
#     # if a == 10:
#     #     break
#     a += 1
#     if a % 2 == 0:
#         continue
#     print(a)

'''
'''
函数调用'''
# def str_combination(str1, str2):
#     str3 = str1 + str2
#     print(str3)
#     return
#
# if __name__ == '__main__':
#     str_combination('abc','def')
    # str1 = str(input("请输入字符串："))
    # str2 = str(input("请输入字符串："))
# 调用不可变型参数
# def Change_para (a):
#     a = 10
#     # print(a)
#     return
# if __name__ == '__main__':
#     b=2
#     Change_para(b)
#     print(b)


#调用可变型参数
# def Change_para (matrx1):
#     matrx1.append(1)
#     # print(matrx1)
#     return matrx1
# Change_para([12,13,14,112])

#必备参数：以正确的顺序传入函数，调用时的数量必须和声明时的一样。
# def Change_para (matrx1):
#     matrx1.append(1)
#     # print(matrx1)
#     return matrx1
# Change_para()

#关键字参数：关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值
# def str_combination(str1, str2):
#     str3 = str1 + str2
#     print(str3,str1)
#     return
# str_combination(str2 =3,str1 =1)

#默认参数：调用函数时，默认参数的值如果没有传入，则被认为默认值
# def str_combination(str1, str2 =3):  #参数在这就已经注明
#     # str2 =3
#     str3 = str1 + str2
#     print(str3,str1)
#     return
# str_combination(str1 =1)

#不定长参数：你可能需要一个函数比当初声明时更多的参数，这些参数叫做不定长参数，声明时不会命名。加了星号*的变量会存放所有未命名的变量参数
# def various_number(arg1,*arg2):
#     print(arg1,arg2)
#     return
# various_number(1,2,3,4,5)

#匿名参数
sum =lambda a,b,c,d: a+b+c

print(sum(1,2,3,4))

