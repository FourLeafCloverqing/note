# 函数
# 字符串拼接
# a = 'string1' + 'string3' + 'string2'
# print(a)


# def test():
#     print('test 函数内 ')
#     # print('a is ', a , 'b is ', b)
#     # result = 'a is %s, b is %s ' % (a, b)
#     # result = 'a is {}, b is {}'.format(a, b)
#     # result = 'a is {}, b is {}'.format(a, b)
#     # print(result)
#     # test_inner('ccccc')
#
#
# return: 结束函数， 并把return后面的值返回, 如果return后面没有值或者没有return， 则默认返回None

def test_return(max):
    # for i in range(1, 200):
    #     if i == 99:
    #         return i * 2
    def test_inner():
        print('执行了里面的函数')
        return "我在里面"

    # 执行里面的函数， 接收返回的字符串
    test_inner_return_value = test_inner()
    return test_inner_return_value


# 可以返回多个值
def test_return_multi_value():
    return '1', '5', '8'


if __name__ == '__main__':
    # print('test 函数外')
    # test()
    return_value = test_return(max='')
    # print(return_value)
    # multi_value = test_return_multi_value()
    # a, b, c  = multi_value
    # print('a is %s, b is %s, c is %s' % (a, b, c))
