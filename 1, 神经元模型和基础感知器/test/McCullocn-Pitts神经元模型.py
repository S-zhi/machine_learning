import dataset
import numpy
from matplotlib import pyplot as plt

xs,ys = dataset.get_beans(100)

w = 1.3
# 在这个模型中 w 需要手动修改 , 没有自动调节功能
y_pre = w * xs
plt.xlabel("x")
plt.ylabel("y_pre")
plt.title("McCulloch-Pitts")
plt.scatter(xs,ys)
plt.plot(xs,y_pre)
plt.show()