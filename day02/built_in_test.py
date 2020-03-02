# abs
# print(abs(-1))
# dict
# print(dict(a=1, b=2))
# print(max(1, 5, 65))
# setattr getattr
class A:
    def method(self):
        print('hell worldl ')
        pass


a = A()
setattr(a, 'test', 'new test value')
setattr(a, 'test2', 'new test value2')
result = getattr(a, 'test3', 111)
# print(result)

# dir : 查看对象的所有方法和属性
# print(dir(a))
# any: 判断一个列表、元祖里面是不是都不为true
item = [None, None, None, None, '', False, 0, '', '   ']
item1 = ['   ', 1, 2, True]


# print(any(item))
# print(all(item1))
#
# for index, value in enumerate(item):
#     print('index is ', index, ', value is ', value)
#
# s = '11+22'
# b = eval(s)
#
# print(b)
class B(A):
    def method(self):
        super(B, self).method()


o = B()

# print(isinstance(o, B))

# print(isinstance(o, A))
# print('hell oworld'.encode())

item = [None, None, None, None, '', False, 0, '', '   ']

# def is_not_none(value):
#     return value is not None

print(list(filter(lambda x: x is not None, item)))


# def test(x):
#     return x + 5

test = lambda x, y: x + y
print(test(5, 100))



print(issubclass(B, A))
print(issubclass(A, B))

print(pow(2, 18))

# callable  判断是否可以调用 , 返回true or  false
print(callable(print))
print(callable(test))
print(callable(2))


# property
class C:
    # @property
    def test(self):
        return "test no property"

    @property
    def test_property(self):
        return 'test property'

    def append(self, x):
        pass

c = C()
print(c.test())
c.append('')
print(c.test_property)


print(type(1))
print(type(c))
print('hello, {}, {}, {}'.format('world', 'world', '......'))
# format()

# map

i = [1, 2, 3, 4, 5]
# i.append('s')
res = list(map(lambda x: x + 1, i))
print(res)

# hasattr
print(hasattr(a, 'method'))
print(hasattr(a, 'll'))
#
print(round(55.2222222222222222222222222222, 2))

