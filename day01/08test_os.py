# 读写文件

# open第一个参数是 文件名(文件路径),  第二个参数是文件打开模式


# r   -> read
# rb  -> read  读二进制
# f = open('test.txt', 'r')
# content = f.read()
# print(content)


# w --> write, 每次写打开并写入的话, 会清空文件并重新写
# wb --> 写二进制
# f = open('test.txt', 'w')
# f.write("1111 New content and  \nnew content and new content \nand new content ... ")

# a --> append, 追加内容
# f = open('test.txt', 'a')
# f.write("\n1111 New content and  \nnew content and new content \nand new content ... ")



# 所有文件都可以使用rb或wb模式打开,
# w和r只可以打开使用记事本打开的文件

# rb 和 wb
# f = open('test.txt', 'rb')
# cont = f.read()
# print(cont)
#



#

# 文件