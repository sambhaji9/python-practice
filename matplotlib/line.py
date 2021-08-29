import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])
ypoints1 = np.array([6, 2, 7, 11])

#plt.plot(ypoints, linestyle='dotted')
plt.plot(ypoints, color='#4caf50')
plt.plot(ypoints1, color='#aabbcc')

plt.show()