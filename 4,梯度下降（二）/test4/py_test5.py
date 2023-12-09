# 本板块内容:
# 1. 完成 点的3D绘制 (py_5)


import dataset
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

xs,ys = dataset.get_beans(100)
ws,ps = dataset.get_beans(100)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# plt.xlim(-2,2)
# plt.ylim(-10,10)
plt.title("number plant")
plt.xlabel("x")
plt.ylabel("y")
ax.scatter(xs,ys,ws)
plt.show()



