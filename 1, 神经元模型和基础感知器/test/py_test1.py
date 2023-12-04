import dataset
import numpy
from matplotlib import pyplot as plt

xs,ys = dataset.get_beans(100)

print(xs)
print(ys)
# 操作1 : 完成 种子生成的操作

plt.title("number plant")
plt.xlabel("x")
plt.ylabel("y")
#plt.scatter(xs,ys)
plt.plot(xs,ys)
# 操作2 ：绘制散点图，绘制直线
plt.show()
