# 1. 传一串数字, 返回所有偶数
# 2. 传一串数字, 返回所有偶数求和
#
# def test_value(*args):
#     result = []
#     for num in args:
#         if num % 2 == 0:
#             result.append(num)
#     return result
#
#
# if __name__ == '__main__':
#     result = test_value(1, 2, 5, 8, 20,3333, 444)
#     print('偶数有', result)


def value_sum (*args):
    sum = 0
    for num in args:
        if num % 2 == 0:
            sum +=num
    return sum
if __name__ == '__main__':
    result = value_sum(1, 2, 5, 8, 20,3333, 444)
    print('和为', result)