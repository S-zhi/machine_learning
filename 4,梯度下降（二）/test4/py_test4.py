# 本程序将要首先的使用 3D 绘图工具对程序所要图形进行绘制
import dataset
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import  Axes3D

m = 100

xs , ys = dataset.get_beans(m)

plt.title("Size-Toxicity Function", fontsize=12)
plt.xlabel('Bean Size')
plt.ylabel('Toxicity')
plt.xlim(0,1)
plt.ylim(0,1.5)
plt.scatter(xs, ys)
plt.show()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_zlim(0,2)

ws = np.arange(0,1,0.01)
for i in range(100) :
    ax.plot_surface( xs[i], ws[i] * xs[i] , 1)
plt.show()