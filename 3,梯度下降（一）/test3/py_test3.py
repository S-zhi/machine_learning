# 本图像的制作,使用调用的plt函数制作动态图像的过程。
import dataset
import numpy as np
from matplotlib import pyplot as plt
xs,ys = dataset.get_beans(100)

ws = np.arange(0,3,0.01)

plt.xlim(2)
plt.ylim(2)
plt.title("number plant")
plt.xlabel("x")
plt.ylabel("y")

for w in ws :
    y_pre = w * xs
    plt.clf()
    plt.xlim(0,2)
    plt.ylim(0,2)
    plt.scatter(xs,ys)
    plt.plot(xs, y_pre)
    plt.pause(0.001)

