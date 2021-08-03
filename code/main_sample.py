# -*- coding: utf-8 -*-
from module import pool_parallel as po
from module import random_sample as ras
import time

# 100000
pool_time = time.time()
<<<<<<< HEAD
po.pool_pal(ras.coin, 10, 100000)
=======
max_num = 100000
result = po.pool_pal(ras.coin, 4, max_num)
>>>>>>> 0e18140c3627316cbbeea9a922ba842b2a8cf70f
end_pool_time = time.time() - pool_time
num0 = result.count(0)
probability = num0 / max_num * 100

#po.pool_pal(ras.dice, 4, 10)

time_no = time.time()
<<<<<<< HEAD
coin_num = []
for i in range(100000):
    coin_num.append(ras.coin(i))
print(coin_num)
=======
for i in range(max_num):
    ras.coin(i)
>>>>>>> 0e18140c3627316cbbeea9a922ba842b2a8cf70f
end_time = time.time() - time_no

print ("並列化あり(pool):{0}".format(end_pool_time) + "[sec]")
print ("並列化なし:{0}".format(end_time) + "[sec]")
print("表が出る確率:{0}".format(probability))