 import matplotlib.pyplot as plt
 N=[]
 t=[]
 dt=1
 a=10
 N.append(1000)
 t.append(0)
 time=30
 for i in range(int(time/dt)):
     temp=N[i]+a*N[i]*dt
     N.append(temp)
     t.append(dt*(i+1))
     print t[-1],N[-1]

 plt.plot(t,N)
 plt.title('population growth trend while b=0') 
 plt.xlabel('time')
 plt.ylabel('number of population')
 plt.show()

