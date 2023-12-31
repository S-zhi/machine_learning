## 机器学习——梯度下降（一）

在正规方程中，单次计算所消耗的时间会大大增加，这样会大大的浪费计算力，为了解决这个问题，我们需要像一个办法吧集中运算转化称为，分布运算，那我们需要像一个问题，对于不同的 **W** 他是存在不同的最优解的，我们可以把单个最优解的和近似的看成总的最优解，这种情况会有一些误差，但是还是可以忽略的。

#### 1，使用单次方差进行更新？

本次我们使用一元一次函数作为研究模型，首先我们能知道，E 的方程的的确确的是一个二次函数，

![image-20231204212536094](D:\machine learning\2,方差代价函数\test\assets\image-20231204212536094.png)   

我们使用这个函数的时候可以进行简化一下就能得到每次单步处理的，这样的时间会大大的减少，并且所有的时间控制都能在我们手中进行控制，避免数据过大导致程序坏死。下面就是单次下我们进行的求W操作

![image-20231205123408902](D:\machine learning\3,梯度下降（一）\test3\assets\image-20231205123408902.png)

这份操作，我们只用计算出每次的最低点的值，让整个的值向整个点递归？这样的思路似乎是可行的，但是在编码上是比较复杂的。所以我们选用另一种方式进行递归

#### 2，梯度（斜率）下降法

斜率下降的意思就是使用斜率作为下滑的指标，由于我们斜率是有正负的更好的向最低点进行趋向，抽象公式如下： 

<center> 斜率公式 ： y =2 * W * X + b </center>

我们每次都使用当前的W值去减去斜率公式的值就可以向终点进行递进，还有上一讲课说的学习率，还要乘上一个正常的学习率整个的代码实现才算正常，如下所示： 

<center> W的更新公式 ： W = W - ( 2 * W * X + b ) * alpha ;</center>

使用整个公式进行多次更新就能完成整个函数的函数更新了，是不是非常巧妙快去动手实践吧





#### 3，扩展性内容

正规方程 + 梯度下降， ---- > sum()
