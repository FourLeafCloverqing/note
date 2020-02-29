# 例子, 使用open实现复制文件   test_file/test.txt   ->  test_file/test1.txt

def test_copy_txt():
    from_file_name = 'test_file/test.txt'
    to_file_name = 'test_file/test1.txt'

    rf = open(from_file_name, 'r')
    content = rf.read()
    rf.close()

    wf = open(to_file_name, 'w')
    wf.write(content)
    wf.close()


def test_copy():
    from_file_name = 'test_file/test.txt'
    to_file_name = 'test_file/test1.txt'

    rf = open(from_file_name, 'rb')
    content = rf.read()  # 读取出来是二进制数据
    rf.close()  # 打开文件, 操作完成后, 必须关闭

    wf = open(to_file_name, 'wb')
    wf.write(content)
    wf.close()



def test_with_open():
    from_file_name = 'test_file/test.txt'
    to_file_name = 'test_file/test1.txt'

    with open(from_file_name, 'r') as rf:
        content = rf.read()

    a = 3
    with open(to_file_name, 'w') as wf:
        wf.write(content)



if __name__ == '__main__':
    test_with_open()
