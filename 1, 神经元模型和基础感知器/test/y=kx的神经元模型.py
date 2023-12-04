import dataset
import numpy
from matplotlib import pyplot as plt

xs , ys = dataset.get_beans(1000)
print(xs)
print(ys)

# 1,完成数据的导入

w = 1.4
y_pro = w * xs
plt.title("f",fontsize = 12)
plt.xlabel("x")
plt.scatter(xs,ys)
# plt.plot(xs,ys)
plt.ylabel("y")

# 2,绘制图像
print(y_pro)

for i in range(10):
    alpha = 0.01
    x = xs[i]
    y = ys[i]
    y_pro = w * x * 0.01
    e = y - y_pro
    w = w + e * alpha  * x

plt.plot(xs,y_pro)
plt.show()