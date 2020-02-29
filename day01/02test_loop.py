# for
# break: for循环中断
# continue:  继续（跳过本次）

# def test_for():
#     for i in range(1, 11):
#         if i == 8:
#             # print('i is 8, break')
#             # break
#             continue
#         print(i)


# while

# continue
# break
def test_while():
    a = 0
    while a < 20:
        # if a == 10:
        #     break
        a += 1
        if a % 2 == 0:
            continue
        print(a)




if __name__ == '__main__':
    test_while()
