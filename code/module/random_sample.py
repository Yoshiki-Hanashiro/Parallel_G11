import time
import random

def coin(x):
    for i in range(x):
        print("num: %d" % x)
        time.sleep(0.2)
        coin_num = random.randint(0,1)
        return(coin_num)