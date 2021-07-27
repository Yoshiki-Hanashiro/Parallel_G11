from time import sleep
import random
from multiprocessing import Process


def coins(count, name):
    for i in range(count):
        print(name+":"+str(i))
        sleep(0.1)
        count_num = random.randint(0, 1)
        print(count_num)


if __name__ == '__main__':
	# coins(100, "main")
    p0 = Process(target=coins, args=(20, "p0"))
    p1 = Process(target=coins, args=(20, "p1"))
    p2 = Process(target=coins, args=(20, "p2"))
    p3 = Process(target=coins, args=(20, "p3"))
    p4 = Process(target=coins, args=(20, "p4"))
    p0.start()
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p0.join()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
