import dataset
import numpy as np
from matplotlib import pyplot as plt

n = 100

xs,ys = dataset.get_beans(n)

E = []

for w in np.arange(0,3,0.01):
    y_pres = w * xs
    es = (y_pres - ys) ** 2
    e_sum = sum(es)
    E.append(e_sum)
    print(e_sum)

plt.title("pow f")
plt.xlabel("x")
plt.xlabel("y")
plt.plot(np.arange(0,3,0.01),E)
plt.show()