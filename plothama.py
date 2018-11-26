import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d


from fuzzy import *

f = fuzzyinterval(6,4,1)
t = np.linspace(-10,10,1000)
x = np.array([f(u) for u in t])

x,y = np.meshgrid(np.linspace(0,1,10),np.linspace(0,1,10))
z = np.array([[Hama(x[i,j],y[i,j]) for j in range(10)] for i in range(10)])
ax = plt.axes(projection='3d')
#plt.axis([-5,10,-0.15,3])
#plt.yscale('linear')
ax.plot_wireframe(x, y, z, color='black')
#plt.grid(True)
#plt.plot(t,x,'r')
plt.show()
