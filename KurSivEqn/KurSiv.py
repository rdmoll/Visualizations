# Kuramoto-Sivashinsky
#
# v_t + v_xx + v_xxxx + vv_x = 0

import numpy as np
import matplotlib.pyplot as plt

numTS = 4096
N = 4096 #2048 #1024
deltaT = 0.05
nImgs = 1 #100

rndNoise = 1.0e-2 * (N/2) * ( 2.0*(np.random.rand( 3 ) - 0.5) + 2.0*(np.random.rand( 3 ) - 0.5)*1j )

for imgIdx in np.arange(nImgs):

    Ln = 32 #(0.1*imgIdx + 22.0)
    L = Ln * 2.0*np.pi

    halfBnd = int(N/2 + 1)
    L2 = L * L
    L4 = L * L * L * L
    pi2 = np.pi * np.pi
    pi4 = np.pi * np.pi * np.pi * np.pi
    diffFac1 = 1j * 2.0 * np.pi / L
    diffFac2 = 4.0 * pi2 * deltaT / L2
    diffFac4 = 16.0 * pi4 * deltaT / L4

    g = np.zeros( [numTS+1, N] ) + np.zeros( [numTS+1, N] )*1j

    x = np.arange( N )
    f0 = np.sin( 16 * 2.0 * np.pi * x / ( 1.0 * N ) )

    F = np.fft.fft( f0 )
    F[1:4] = F[1:4] + rndNoise
    #F[0] = 0.0 + 0.0*1j

    dF = np.zeros(N) + np.zeros(N)*1j
    df = np.zeros(N) + np.zeros(N)*1j
    nl = np.zeros(N) + np.zeros(N)*1j
    NL = np.zeros(N) + np.zeros(N)*1j

    derivFac = np.zeros(N) + np.zeros(N)*1j
    solveFac = np.zeros(N) + np.zeros(N)*1j

    for j in np.arange( halfBnd ):
        derivFac[ j ] = j * diffFac1
        solveFac[ j ] = 1.0 / ( 1.0 - diffFac2 * j**2 + diffFac4 * j**4 )

    for j in np.arange( halfBnd, N ):
        derivFac[ j ] = -(N-j) * diffFac1
        solveFac[ j ] = 1.0 / ( 1.0 - diffFac2 * (N-j)**2 + diffFac4 * (N-j)**4 )

    for i in np.arange( numTS ):
        dF = derivFac * F

        f = np.fft.ifft( F )
        df = np.fft.ifft( dF )
        nl = f.real * df.real
        NL = np.fft.fft( nl )

        g[i,:] = f

        F = solveFac * ( F - deltaT*NL )

    g[numTS,:] = f
    #plt.imshow( g.real, aspect='equal' )
    #plt.savefig("./frames/screen-{:04}.tif".format(imgIdx))

#plt.imshow( g.real, aspect='equal' )
#plt.imshow( g.real, cmap='magma', aspect='equal' )
#plt.imshow( g.real, cmap='bone', aspect='equal' )
#plt.imshow( g.real, cmap='winter', aspect='equal' )
#plt.imshow( g.real, cmap='binary', aspect='equal' )

plt.imshow( g.real, cmap='twilight', aspect='equal' )
plt.axis('off')
plt.savefig("test1.tif", bbox_inches='tight', dpi=1200.0)

plt.imshow( g.real, cmap='gist_gray', aspect='equal' )
plt.axis('off')
plt.savefig("test2.tif", bbox_inches='tight', dpi=1200.0)

plt.show()
