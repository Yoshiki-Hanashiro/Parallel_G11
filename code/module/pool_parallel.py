# -*- coding: utf-8 -*-
from multiprocessing import Pool
from . import random_sample as ras


# 並列処理させる関数
def pool_pal(parallel, proc, pal_num=10):
    p = Pool(proc)
    result = p.map(parallel,range(1,pal_num + 1))
    return result


if __name__ == "__main__":
    pool_pal(ras.coin,4,3)