import time
import random
from multiprocessing import Pool

# 並列処理させる関数
def coin(x):
    for i in range(x):
        print("num: %d" % x)
        time.sleep(2)
        coin_num = random.randint(0,1)
        return(coin_num)
    
if __name__ == "__main__":
    p = Pool(4) # プロセス数を4に設定
    result = p.map(coin, range(10))  # nijou()に0,1,..,9を与えて並列演算
    print(result)