##一、second day（语言元素）
1.变量数据类型主要包括浮点型、整数型、布尔型、字符串

int():将一个数值或者变量转换为整数型

float():将一个数值或者变量转换为小数型（浮点型）

str():将变量或者数值转换为字符型

chr():将整数转换成对应的字符串

ord():将字符串转换成对应的数字

2.运算符号：+ - * / ** %  //  ==

3.print语句输出括号里的形式：print ("*** %d" %(变量名称)) 注意：%后跟的是变量类型的形式 d s f

4.输出pi语句：import math    
math.pi




##二、 git

1. git init
初始化

2. git status    

状态

3. git add file_name
添加到暂存区

4. git commit -m '第一次提交代码'
提交到版本库

5. git log   
查看提交历史

6. git reset --hard  版本号
回滚代码， 新代码会被删除

7. git reset --soft 版本号
回滚代码， 新代码会不被删除


8. git push orgin master 

提交到远程仓库

##三、third_day（分支结构）
1. if elif else依次递进，并且均在后面加冒号，注意缩进

##四、forth_day（循环结构）
1.计算机生成一个随机数语句：import random 

random = random.radint(数的取值范围)

2.当构建一个不知道循环次数的语句时，应采用while语句，while True:表示接着循环，
然后设定当不满足条件时会怎样

3.案例：计算机随机生成一个数，邀请一个人来猜，分别给出“猜大了”、“猜小了”和“恭喜您猜对了”，
当猜测次数大于7次时，则提醒“该重新学习了”。

```import random
answer = random.randint(1,100)
count = 0
while True:
    guess = int(input('请猜一下这个数'))
    if guess > answer:
        print('您猜的数大了一些')
    elif guess < answer:
        print('您猜的数小了一些')
    else:
        print('恭喜您猜对了')
        break
    count +=1
    print('您一共答题%d次' %count)
if count >7:
    print('您应该学习了')
```


4.案例：输出乘法口诀表
```
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d'%(i,j,i*j),end='\t')
    print()
  
```