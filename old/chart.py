import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import numpy as np

df = pd.read_csv('DE10.csv')
data2d = df.values

#rows = np.where((data2d[:, 1] == 0.75) & (data2d[:, 2] == 0.9))
print(data2d[rows,6])


x = data2d[:,1]
y = data2d[:,2]
z = data2d[:,6]
x = np.reshape(x,(20, 20))
y = np.reshape(y,(20, 20))
z = np.reshape(z,(20, 20))
print(x)
plt.pcolormesh(x, y, z)
#dz = data2d[:,6]

fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

#ax.bar3d(x, y, z, dx, dy, dz)
fig.savefig('PopEMQ.png')
