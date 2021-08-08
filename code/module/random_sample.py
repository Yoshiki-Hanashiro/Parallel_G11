import time
import random

def coin(x):
    print("\r"+"num: %d" % x, end=" ")
    #time.sleep(0.2)
    coin_num = random.randint(0,1)
    return(coin_num)

def dice(x):
    for i in range(x):
        print("num: %d" %i)
        time.sleep(0.2)
        dice_num = random.randint(1,6)
        return(dice_num)