import time
import random

def coin(x,sleep_time = 0):
    print("num: %d" % x)
    time.sleep(sleep_time)
    coin_num = random.randint(0,1)
    return(coin_num)

def dice(x,sleep_time = 0):
    print("num: %d" % x)
    time.sleep(sleep_time)
    dice_num = random.randint(1,6)
    return(dice_num)