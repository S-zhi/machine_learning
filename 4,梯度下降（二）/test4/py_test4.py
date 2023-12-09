# 二维平面中的曲线的画法
import dataset
import numpy as np
from matplotlib import pyplot as plt

xs,ys = dataset.get_beans(100)


plt.title("number plant")
plt.xlabel("x")
plt.ylabel("E")
plt.scatter(xs,ys)
for b in np.arange(1,1.9 , 0.01):
    e = []
    ws = []
    for w in np.arange(-1,1,0.04):
        y_pre = xs * w + b
        E = np.sum((y_pre - ys )**2)
        e.append(E)
        ws.append(w)
    plt.plot(ws,e)
plt.show()
