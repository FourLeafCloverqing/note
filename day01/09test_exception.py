# python的异常
# 异常捕获


def test():
    try:
        a = [123,5]
        # a[4]  # IndexError
        # a = 1 / 0  # 异常  ZeroDivisionError
        # open('tfdsfa.jpg')   # FileNotFoundError
        # print('jkj')
    except ZeroDivisionError:
        print('除数不可以是0  ')
    except FileNotFoundError:
        print('文件不存在')
    except Exception:
        print('其他异常')
    finally:
        print('finally 中的语句  .. ')
    print('hello world')


def test1():
    print('hello your world !~ ')

def test_open_and_close(file_name):
    f = open(file_name, 'r')
    try:
        conent = f.read() # 程序出错了
    finally:
        f.close()

if __name__ == '__main__':
    # test()
    test1()
    test_open_and_close('test_file/test.txt')
