#################
##
## Perlin noise
##
#################

import numpy as np
from scipy.interpolate import Rbf
import matplotlib.pyplot as plt

numRows = 64
numCols = 64
A = np.zeros( [numRows, numCols] )
dAdx = np.zeros( [numRows, numCols] )
dAdy = np.zeros( [numRows, numCols] )

seedRows = 4
seedCols = 4
rndPhase = np.pi * 2.0 * np.random.rand( seedRows, seedCols )
for i in np.arange( seedRows ):
    for j in np.arange( seedCols ):
        dAdx[16*i + 8,16*j + 8] = np.cos( rndPhase[i,j] )
        dAdy[16*i + 8,16*j + 8] = np.sin( rndPhase[i,j] )

rbf = Rbf(x, y, z, epsilon=2)
ZI = rbf(XI, YI)

for i in np.arange( numRows ):
    for j in np.arange( numCols ):


plt.imshow( A, cmap='twilight', aspect='equal' )
#plt.pcolormesh(X_edges, Y_edges, ZI, shading='flat', **lims)
plt.axis('off')
plt.savefig("test.tif", bbox_inches='tight', dpi=1200.0)

plt.show()
