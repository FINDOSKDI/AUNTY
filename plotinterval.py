import matplotlib.pyplot as plt
import numpy as np
from fuzzy import *

f = fuzzyinterval(6,4,1)
t = np.linspace(-10,10,1000)
x = np.array([f(u) for u in t])

plt.axis([-5,10,-0.15,3])
plt.yscale('linear')
plt.grid(True)
plt.plot(t,x,'r')
plt.show()
