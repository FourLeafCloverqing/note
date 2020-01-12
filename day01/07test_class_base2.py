# 实例方法, 实例属性
#  属于类的对象


# 类方法, 类属性
# 类方法和类属性属于类
# 类的对象可以调用类方法, 获取类属性

# 静态方法 : 不属于类, 也不属于对象,
# 类和类的对象都可以调用静态方法

# 类
class Person:
    a = 90  # 类属性

    def __init__(self):
        self.name = 'a'

    def battle(self):
        print('battle')

    # 方法
    def run(self):
        # self 就是 实例化的对象
        self.battle()
        print('两条腿跑.')

    # 类的方法
    @classmethod
    def test(cls):
        # cls就是Person类
        print('cls.a', cls.a)
        print('类test方法.')

    @staticmethod
    def test_static():
        # 没有cls和cls
        print('这不可以使用cls和self')


if __name__ == '__main__':
    # 类的对象, p
    # p = Person('xx', 1)
    # p.run()
    # print(Person.a)
    # Person.test()

    # p = Person()
    # p.test()
    # p.run()
    # p.test_static()
    Person.test()

