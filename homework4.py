>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> def f(x0,n):
...         v=40
...         t=np.arange(0.0,5.0,5.0/n)
...         plt.plot(t,x0+v*t,'bo',t,x0+v*t,'k')
...         plt.title('$Problem1.2$',fontsize=28)
...         plt.xlabel('$t$',fontsize=20)
...         plt.ylabel('$X(t)$',fontsize=20)
...         plt.show()
... 
>>> f(10,10)

