# 本次首先练习使用python解决求单次均方差的问题
import dataset
import numpy

xs,ys = dataset.get_beans(100)

w = 1.28

y_pres = w * xs

es = (y_pres - ys)**2

e_sum = sum(es)

print("E:"+str(e_sum))