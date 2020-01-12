# 1. 面向过程
# 2. 面向对象

# class

# 类
# 入门
class Person:
    #  __init__ 构造方法
    def __init__(self, name, age):
        # name和age是属性
        print('创建了一个人')
        self.name = name
        self.age = age
        self.hp = 100

    def battle(self, other):
        if other.hp < 0:
            print(f'{other.name}已经死亡, 不要再打了')
            return
        other.hp -= 1
        if other.hp < 0:
            print(f'{other.name}的hp -1 , 已经死亡, 剩余: {other.hp}')
        else:
            print(f'{other.name}的hp -1 , 剩余: {other.hp}')

    def xxx(self):
        print('不知道干嘛')


    def run(self):
        print('两条腿跑.')


class Animal:
    def run(self):
        print('四条腿跑.. ')


# 继承, 多继承
class Singer(Animal, Person):
    def sing(self, content):
        print(f'{self.name}  唱道: {content}')

    def battle(self, other):
        print('歌手也可以打架 ')
        super(Singer, self).battle(other)

    def __init__(self, name, age, product):
        super(Singer, self).__init__(name, age)
        self.product = product


# 人 -> 名字年龄性学校 , 吃饭说话走路

if __name__ == '__main__':
    # 创建对象(caixukun)
    caixukun = Singer('蔡徐坤', 12, '鸡你太美')
    caixukun.sing("我唱了唱了唱了... ")
    caixukun.run()
    # print(caixukun.age)
    # print(f'{caixukun.name} 的初始化hp值 {caixukun.hp}')
    # wuyifan = Singer('吴亦凡', 21, '大碗宽面')
    # print(f'{wuyifan.name} 的初始化hp值 {wuyifan.hp}')
    #
    # for i in range(103):
    #     caixukun.battle(wuyifan)
