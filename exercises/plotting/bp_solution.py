import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0,2*np.pi,50)
b = np.sin(a)

plt.plot(a,b)

mask=b>=0

plt.plot(a[mask],b[mask],'rx')

plt.show()