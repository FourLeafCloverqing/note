# 线程
from threading import Thread

# 进程
from multiprocessing import Process


# 如果,你烧水,
# 打水,插电, 等十分钟,你就是干等 啥都不干, 就是单线程
# # 打水插电, 等的过程中, 还在刷微博, 你就是多线程...
# import time
#
# def boil_water():
#     print('烧水, 等待十秒钟')
#     time.sleep(20)
#     print('开了')
#
#
# def word(number):
#     print('记单词: ', number, '个')
#
#
# if __name__ == '__main__':
#     boil_water_task = Thread(target=boil_water)
#     word_task = Thread(target=word, args=(100, ))
#     boil_water_task.start()
#     word_task.start()

# i = 0
for i in  range(1,5):
    print(i)


