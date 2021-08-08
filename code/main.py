# -*- coding: utf-8 -*-
from module import pool_parallel as po
from module import random_sample as ras
import time
import os

pool_time = time.time()
max_num = 100000
print("----------------------------" + "\n" + "処理を並列化ありで実行中")
result = po.pool_pal(ras.coin, 4, max_num)
end_pool_time = time.time() - pool_time
num0 = result.count(0)
probability = num0 / max_num * 100

#po.pool_pal(ras.dice, 4, 10)

time_no = time.time()
print("\n" + "----------------------------" + "\n" + "処理を並列化なしで実行中")
for i in range(max_num):
    ras.coin(i)
end_time = time.time() - time_no
print("\n" + "--------------------------------------------")
print ("並列化あり(pool):{0}".format(end_pool_time) + "[sec]")
print ("並列化なし:{0}".format(end_time) + "[sec]")
print ("コインの表が出た確率:{0}".format(probability) + "\n")

# ファイルに書き込み
current_path = os.getcwd()
with open(current_path+"/log_file", mode='a') as f:
    f.write("並列化あり(pool):{0}".format(end_pool_time) + "[sec]"+ "\n")
    f.write("並列化なし:{0}".format(end_time) + "[sec]"+ "\n")
    f.write("コインの表が出た確率:{0}".format(probability) + "\n" + "\n")
