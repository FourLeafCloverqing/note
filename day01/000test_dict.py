# 字典: key --> value

# 字典的遍历




def test_dict():
    pass


if __name__ == '__main__':
    a = {
        'name': 'z',
        'age': 111,
        'gender': 'f',
        'marks': "helfjlfdj"
    }

    # # 遍历字典的key
    # for i in a.keys():
    #     print(i)
    # # 遍历字典的value
    #
    #
    # for i in a.values():
    #     print(i)
    #
    for i, j in a.items():
        print('字典的key: {} --> value: {}'.format(i,  j))
