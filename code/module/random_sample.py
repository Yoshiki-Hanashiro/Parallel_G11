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

