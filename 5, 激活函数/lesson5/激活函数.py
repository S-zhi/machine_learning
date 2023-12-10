# y = w * x + b
import dataset
import numpy as np
from matplotlib import pyplot as plt

xs,ans = dataset.get_beans(100)

plt.title("number plant")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(0,2)
plt.ylim(0,2)

w = 1
b = 0
alpha = 0.1

for j in range(10000):
    for i in range(100):

        x = xs[i]
        a1 = ans[i]
        # 我们知道的是仅仅是 对每个变量的分析是不同的所以我们进行分布计算即可
        dydw = x
        y = x * w + b
        a = 1/(1+np.exp(-y))
        dady = a*(1-a)
        # (y-a)**2
        deda = -  2 * a1 + 2 * a
        dedw = deda * dady * dydw
        w = w - dedw  * alpha
        dydb = 1
        dedb = deda * dady * dydb
        b = b - dedb * alpha
    if j % 100 == 0 :
        y = w * xs + b
        a = 1/(1+np.exp(-y))

        plt.clf()
        plt.xlim(0, 1)
        plt.ylim(0, 1.5)
        plt.scatter(xs,ans)
        plt.plot(xs,a)
        plt.pause(0.01)
plt.show(5)