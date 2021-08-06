from time import sleep
import random
from multiprocessing import Process


def coins(count, name):
    number_list = []
    for i in range(count):
        print(name+":"+str(i))
        sleep(0.2)
        number_list.append(random.randint(0, 1))
    print(number_list)
    return number_list


def process(process_number, num):
    # num:プロセス数
    p_list = []
    for i in range(process_number):
        p = Process(target=coins, args=(num, "p"+str(i)))
        p.start()
        p_list.append(p)

    # プロセスの終了
    for j in p_list:
        j.join()
    return p_list


if __name__ == '__main__':
    # coins(50000, "main")
    process(10, 10)
