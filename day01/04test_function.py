# 不定长的意思就是: 可以传任意长度的参数
#  函数的不定长参数, 使用*args, 或者**kwargs
# *args: 接收过来是个tuple
# **kwargs: 接收过来是dict


# def test(*a):
#     # 接收过来的值是： (12, 2, 2, 43, 5, 6), 元组
#     print(a)
#     for i in a:
#         pass
#     print('我在函数里面')


def sum_value(*args):
    total = 0
    for i in args:
        total += i
    return total


def test_kwargs(a, b, **kwargs):
    print(type(kwargs))
    print('a: %s, b: %s kwargs: %s ' % (a, b, kwargs))
    # kwrags: {'c': 2, 'd': 4, .......}
    # b:
    c = kwargs.get('c')
    print('c is ', c)


def test_args_and_kwargs(m, n, *args, **kwargs):
    # print('m is {}, n is {}, args: {}, kwargs: {}'.format(m, n, args, kwargs))
    print(f'm is {m}, n is {n}, args: {args}, kwargs: {kwargs}')


if __name__ == '__main__':
    # total_value = sum_value(1, 2, 5, 6, 67, 7, 7, 2, 231, 1)
    # print('sum:   {}'.format(total_value))
    # test_kwargs(1, 3, c=2, d=4, e=5, f=6)
    test_args_and_kwargs('mmmmm', 'nnnnnn', 'xxxxx', 'yyyyyy', x=3, y=4, max=9)
