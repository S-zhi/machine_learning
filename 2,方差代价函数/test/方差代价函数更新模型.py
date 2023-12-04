import dataset
import numpy as np
from matplotlib import pyplot as plt

n = 100

xs,ys = dataset.get_beans(n)

xys = sum(xs*ys)
xxs = sum(xs*xs)

print(xys/xxs)
w = xys / xxs
y_pre = w * xs
plt.xlabel("x")
plt.ylabel("y_pre")
plt.title("pow_f")
plt.scatter(xs,ys)
plt.plot(xs,y_pre)
plt.show()