from module import pool_parallel as po
from module import random_sample as ras
import time

pool_time = time.time()
po.pool_pal(ras.coin, 4, 100000)
end_pool_time = time.time() - pool_time

#po.pool_pal(ras.dice, 4, 10)

time_no = time.time()
for i in range(100000):
    ras.coin(i)
end_time = time.time() - time_no

print ("並列化あり(pool):{0}".format(end_pool_time) + "[sec]")
print ("並列化なし:{0}".format(end_time) + "[sec]")