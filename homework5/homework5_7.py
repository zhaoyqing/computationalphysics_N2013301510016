 import matplotlib.pyplot as plt
 N=[]
 t=[]
 dt=5.
 a=10.
 b=0.1
 N.append(1000.)
 t.append(0.)
 time=5.
 for i in range(int(time/dt)):
     temp=N[i]+(a*N[i]+b*N**2)*dt
     N.append(temp)
     t.append(dt*(i+1))

 plt.plot(t,N)
 plt.title('population growth trend while b=0.1') 
 plt.xlabel('time')
 plt.ylabel('number of population')
 plt.show()

