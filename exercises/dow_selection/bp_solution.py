import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('dow.csv',delimiter=',')
OPEN,HIGH,LOW,CLOSE,VOLUME,ADJ_CLOSE = range(6)

mask_ind = np.where(data > 5.5 * 10**9)[0]
mask = data > 5.5 * 10**9
cnt = sum(mask)

print(data.size)

print(data[:,ADJ_CLOSE][mask_ind],cnt)

plt.plot(data[:,ADJ_CLOSE])
plt.plot(mask_ind,data[mask_ind,ADJ_CLOSE],'rx')
plt.show()

