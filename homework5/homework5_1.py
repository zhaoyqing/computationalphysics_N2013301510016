 import numpy as np
 import matplotlib.pyplot as plt
 t=np.arange(0,30,1)
 y=1000*np.exp(10*t)
 
 plt.plot(t,y,'r')
 plt.title('population growth trend while b=0')
 plt.xlabel('time')
 plt.ylabel('the number of population')
 plt.show()

