import time
import random
from multiprocessing import Pool

def coin(x):
    print("num: %d" % x)
    time.sleep(2)
    coin_num = random.randint(0,1)
    return(coin_num)

def dice(x):
    print("num: %d" % x)
    time.sleep(2)
    dice_num = random.randint(1,6)
    return(dice_num)

def find_divisor(number):
    Prime = False
    for k in range(1,number):
        if k == 1:
            continue
        elif number % k == 0:
            Prime = True

    return Prime

def parallel(x):
    return x**2

def no_parallel(x):
    return x**2


##並列化あり
if __name__ == "__main__":
     for j in range(1,11):
        p = Pool(j)
        start = time.time()
        x =sum(p.map(parallel,range(1,10000000)))
        elapsed_time = time.time() - start
        print("並列化(プロセス数:{}){}[sec]".format(j,elapsed_time))
        print("count={}".format(x))
##並列化無し
     start = time.time()
     count = 0
     for i in range(1, 10000000):
        count += no_parallel(i)
     elapsed_time = time.time() - start
     print("並列化無し:{0}[sec]".format(elapsed_time))
     print("count={}".format(count))








