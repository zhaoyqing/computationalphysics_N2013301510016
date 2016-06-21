 import matplotlib.pyplot as plt
 N=[]
 t=[]
 dt=5.
 a=10
 b=0.000001
 N.append(1000.)
 t.append(0.)
 time=10.
 for i in range(int(time/dt)):
     temp=N[i]+(a*N[i]-b*N[i]**2)*dt
     N.append(temp)
     t.append(dt*(i+1))

 plt.plot(t,N)
 plt.title('population growth trend while b=0.000001') 
 plt.xlabel('time')
 plt.ylabel('number of population')
 plt.show()

