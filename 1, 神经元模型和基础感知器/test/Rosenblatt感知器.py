import dataset
import numpy
from matplotlib import pyplot as plt

xs,ys = dataset.get_beans(100)

w = 0.5

y_pre = w * xs
alpot = 0.01
for m in range(1,100):
    for i in range(1,100):
        e = ys[i] - y_pre[i]
        w = w + e * xs[i] * alpot
        print(w)
        y_pre = w * xs
plt.xlabel("x")
plt.ylabel("y_pre")
plt.title("Rosenblatt")
plt.scatter(xs,ys)
plt.plot(xs,y_pre)
plt.show()