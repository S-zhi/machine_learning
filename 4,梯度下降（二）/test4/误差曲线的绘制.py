# 完成误差曲线的绘制
import dataset
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

xs,ys = dataset.get_beans(100)

plt.title("number plant")
plt.xlabel("x")
plt.ylabel("y")

ws = np.arange(0,2,0.01)
bs = np.arange(0,4,0.01)
fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')
# ax.set_xlim(3)
# ax.set_ylim(3)
# ax.set_zlim(3)
# # plt.xlim(0,4)
# # plt.ylim(0,4)
alpha = 0.01
for b in bs :
    E = []
    B = []
    for w in ws :
        y_pre = w * xs + b
        e = sum((ys-y_pre)**2)
        E.append(e)
        B.append(b)
    ax.plot(B,ws,E)
plt.show()