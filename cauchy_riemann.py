import numpy as np

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

#meshsize

N=100

U = np.zeros([N,N])

V = np.zeros([N,N])

# dirichlet bc

x = np.linspace(0,2*np.pi,N)

xSize = np.pi * 2


for n in range(0,N):

    V[N-1,n] = np.cos(x[n])

    U[N-1,n] = np.sin(x[n])



# recursion

for i in range(1,N-1):

    for j in range(0,N-1):

        U[i,j] = U[i,j+1] - V[i+1,j] + V[i,j]

        V[i,j] = U[i+1,j] - U[i,j] + V[i,j+1]

        #periodic bc

        dx1 = x[j] - x[i]

        dx = np.mod(dx1, xSize * 0.5)

        V[i-1, 0] = dx

        U[i-1, 0] = dx

        V[i-1, N-1] = dx

        U[i-1, N-1] = dx


# coordinates

x = range(N)

y = range(N)

x, y = np.meshgrid(x, y)



# for interactive plot

#%matplotlib notebook



# create plot

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, U, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
