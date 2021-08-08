import time
import random

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

def find_divisor(number,R):
    OK= 0
    for k in range(R,number+1):
        if number % k == 0:
            OK = 1
            print("number = {}".format(k))
            break
    return(OK)
##約数の個数をカウントするメソッド　これは約数の一つを見つけたら終了する感じ
##これをnumberの数だけ実行できるようにする
