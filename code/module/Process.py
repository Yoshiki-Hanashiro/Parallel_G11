from time import sleep
import random
from multiprocessing import Process
from multiprocessing import Array
# process(プロセス数,コインを回す回数)で実行できる

def coins(count, name, arr):
    for j in range(count):
        if(j<5):
            print("p"+str(name)+":"+str(j))
        # sleep(0.2)
        arr[name*count+j] = random.randint(0, 1)


def process(process_count, coin_count):
    process_list = []
    arr = Array('i', range(process_count*coin_count))
    num = int(coin_count / process_count)
    for i in range(process_count):
        p = Process(target=coins, args=(num, i, arr))
        p.start()
        process_list.append(p)

    for j in process_list:
        j.join()
    return arr[:]


if __name__ == "__main__":
    print(process(4, 100))
