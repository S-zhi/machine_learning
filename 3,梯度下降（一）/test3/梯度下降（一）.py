import dataset
import numpy as np
from matplotlib import pyplot as plt

xs,ys = dataset.get_beans(100)

w = 0.5
y_pre = w * xs

plt.title("number plant")
plt.xlabel("x")
plt.ylabel("y")

alpha = 0.05
plt.show()
for m in range(100):
    for i in range(100):
        w = w - alpha * (2 * w * xs[i]**2 - 2 * xs[i] * ys[i] )
        y_pre = w * xs
        plt.clf()
        plt.xlim(0,1)
        plt.ylim(0,1.5)
        plt.plot(xs,y_pre)
        plt.scatter(xs,ys)
        plt.pause(0.01)


