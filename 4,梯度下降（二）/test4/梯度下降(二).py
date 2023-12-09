import dataset
import numpy as np
from matplotlib import pyplot as plt

xs,ys = dataset.get_beans(100)

plt.title("number plant")
plt.xlabel("x")
plt.ylabel("y")
# y_pre = a * x + b


a = 1

b = 0

alpha = 0.1


# 对 a : 2 * x * a + ( b - y )

for j in range(100):
    for i in range(100):
        x = xs[i]
        y = ys[i]
        dw = 2 * x ** 2 * a + 2 * x * b - 2 * x * y
        db = 2 * b + 2 * a * x - 2 * y
        b = b - db * alpha
        a = a - alpha * dw
        y_pre = a * xs + b
    plt.clf()
    plt.scatter(xs,ys)
    plt.plot(xs,y_pre)
    plt.pause(0.01)
