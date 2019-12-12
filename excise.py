#Second_day
# f = int (input('请输入华氏温度'))
# c =  (f - 32) / 1.8
# print("华氏温度为 %d = 摄氏温度为 %.1f" % (f,c)
# print('%.d华氏度 = %.1f摄氏度' % (f, c))
# print(c)
# f = float(input('请输入华氏温度: '))
# c = (f - 32) / 1.8
# print('华氏度 %.1f = 摄氏度 %.1f' % (f, c))
# import math
# r = float (input('请输入圆的半径'))
# s = math.pi * r ** 2
# l = 2 * math.pi *r
# print("圆的周长为 %.2f,圆的面积为 %.2f" %(s,l))
# # print('周长: %.2f' % perimeter)
# print('面积: %.2f' % area)

##third_day
# x = float (input('请输入x值'))
# if x > 1:
#     f = 3 * x - 5
# elif (x >= -1 and x <= 1):
#     f = x + 2
# else:
#     f = 5 * x + 3
# print(f)

# long = float(input('请输入长度：'))
# unit = str(input('请输入长度所对应的单位：'))
# if unit == 'in':
#     print("%.1f英寸 = %.1f厘米" %(long, 2.54 * long))
# else:
#     print("%.1f厘米 = %.1f英寸" %(long, long / 2.54))


##forth_day
# i = 1
#
# for j in range(2,100):
#     # i = i + j
#     i += j
# print(i)

# import random
# answer = random.randint(1,100)
# count = 0
# while True:
#     guess = int(input('请猜一下这个数'))
#     if guess > answer:
#         print('您猜的数大了一些')
#     elif guess < answer:
#         print('您猜的数小了一些')
#     else:
#         print('恭喜您猜对了')
#         break
#     count +=1
#     print('您一共答题%d次' %count)
# if count >7:
#     print('您应该学习了')
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d*%d=%d'%(i,j,i*j),end='\t')
#     print()
# j=1
# for i in range(1,3):
#     j += i
# print(j)



## fifth_day
# （水仙花）
# for num in range (100,1000):
#     i = num //100
#     j = num // 10 % 10
#     k = num % 150
#     if num ==(i ** 3 + j ** 3 + k ** 3):
#         print("%d 是水仙花数" %num)

#正整数反转
num = str(input("请输入一个正整数："))
# num_roll = num[::-1]
# print(num[::-1])
# str = 'abcdef'
print(num[::-1])