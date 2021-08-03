from multiprocessing import Pool
from . import random_sample as ras


# 並列処理させる関数
def pool_pal(parallel, proc, pal_num=10):
    p = Pool(proc) # プロセス数を4に設定
    #parallel = "ras." + parallel
    #print(parallel)
    #result = p.map(eval(parallel),range(pal_num))
    result = p.map(parallel,range(1,pal_num + 1))
    print(result)
    return result


if __name__ == "__main__":
    pool_pal(ras.coin,4,3)