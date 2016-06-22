#第五次作业
##摘要
用欧拉法解决人口问题的模型
##背景
人口增长问题往往会产生一阶速率方程，例如：<br/>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7BdN%7D%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3DaN-bN%5E%7B2%7D)<br/>
上述方程能描述一个群体中的个体数N，随时间的变化而变化，方程中的第一项aN对应于人口的出生率，而第二项-bN^2则对应于人口的死亡率，人口的死亡率与N^2是成正比的
，因为实际上当人口增多，即N变大时，食物会更加难以找到。用欧拉法解决当b=0时的上述的方程，并将所得的结果与精确解进行比较。然后用再解决
b不为0的情况，对结果进行一个直观的解释。a，b的值取决于人口N的初始值，对于很小的N（0），a=10,b=3；对于N=1000,a=10,b=0.01。
##正文
用欧拉法对方程进行泰勒展开有
![](http://latex.codecogs.com/gif.latex?N%28%5CDelta%20t%29%3DN%280%29&plus;%5Cfrac%7BdN%7D%7Bdt%7D%5CDelta%20t&plus;%5Cfrac%7B1%7D%7B2%7D%5Cfrac%7B%5Cmathrm%7Bd%5E2%7D%20N%7D%7B%5Cmathrm%7Bd%7D%20t%5E2%7D%28%5CDelta%20t%29%5E2&plus;%5Cfrac%7B1%7D%7B6%7D%5Cfrac%7B%5Cmathrm%7Bd%5E3%7D%20%7D%7B%5Cmathrm%7Bd%7D%20t%5E3%7D%28%5CDelta%20t%29%5E3&plus;)……<br/>
取一级近似，得<br/>
![](http://latex.codecogs.com/gif.latex?N%28%5CDelta%20t%29%5Capprox%20N%280%29&plus;%28aN-bN%5E2%29%5CDelta%20t)<br/>
#####b=0
在理想条件下，当人类生活的空间足够大，食物足够丰富，不受任何疾病威胁等等，即人口增长不受任何条件限制时，人口死亡率为0,人口增长率
只与人口出生率有关，此时，方程变为<br/>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7BdN%7D%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3DaN)<br/>
取N(0)=0,t=30
 - 不使用欧拉法时的人口增长<br/>
由方程有，<br/>
![](http://latex.codecogs.com/gif.latex?%5Cint%20%5Cfrac%7BdN%7D%7BN%7D%3D%5Cint%20adt)
得 ![](http://latex.codecogs.com/gif.latex?lnN-lnN%280%29%3Dat)<br/>
人口N的增长方式为：<br/>
![](http://latex.codecogs.com/gif.latex?N%3DN%280%29e%5E%7Bat%7D)<br/>
人口增长趋势图：<br/>
![](https://github.com/zhaoyqing/computationalphysics_N2013301510016/blob/master/homework5/homework5_1.png)<br/>
[代码1](https://github.com/zhaoyqing/computationalphysics_N2013301510016/blob/master/homework5/homework5_1.py)<br/>
 - 使用欧拉法时的人口增长<br/>
此时方程变为<br/>
![](http://latex.codecogs.com/gif.latex?N%28%5CDelta%20t%29%5Capprox%20N%280%29&plus;aN%5CDelta%20t)<br/>
趋势图：<br/>
![](https://github.com/zhaoyqing/computationalphysics_N2013301510016/blob/master/homework5/homework5_2.png)<br/>
[代码2](https://github.com/zhaoyqing/computationalphysics_N2013301510016/blob/master/homework5/homework5_2.py)<br/>
由以上两种情况比较，精确解的情况为，先缓慢增长，到了某个时间点突然开始急速增长；而欧拉法的情况则是，先是缓慢增长，然后快速增长，最后急速增长。两者情况相似，到最后都是呈爆炸式增长。

####b不为0
欧拉法得到方程为<br/>
![](http://latex.codecogs.com/gif.latex?N%28%5CDelta%20t%29%3DN%280%29&plus;%28aN&plus;bN%5E2%29%5CDelta%20t)<br/>
令N=1000,a=10,b=0.01<br/>
得到的趋势图为<br/>
![](https://github.com/zhaoyqing/computationalphysics_N2013301510016/blob/master/homework5/homework5_3.png)<br/>
[代码3](https://github.com/zhaoyqing/computationalphysics_N2013301510016/blob/master/homework5/homework5_3.py)<br/>
可见，这种情况下，人口出生率等于死亡率，人口不增加也不减少
令b=0.1<br/>
![](https://github.com/zhaoyqing/computationalphysics_N2013301510016/blob/master/homework5/homework5_7.png)<br>
[代码4](https://github.com/zhaoyqing/computationalphysics_N2013301510016/blob/master/homework5/homework5_7.py)<br/>
这种情况下，人口死亡率大于出生率，人口数量迅速减少，直至完全为0
令b=0.000001<br/>
![](https://github.com/zhaoyqing/computationalphysics_N2013301510016/blob/master/homework5/homework5_5.png)<br/>
![](https://github.com/zhaoyqing/computationalphysics_N2013301510016/blob/master/homework5/homework5_6.png)<br/>
[代码5](https://github.com/zhaoyqing/computationalphysics_N2013301510016/blob/master/homework5/homework5_5.py)<br/>
这种情况下，人口数量一开始迅速上升，死亡率小于出生率，但随着时间的推移，死亡率逐渐上升且将超过出生率，导致人口到达饱和之后急速
下降。

##结论
在正文中
##致谢
感谢班上的同学们的代码～

