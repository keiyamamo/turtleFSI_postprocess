from dolfin import *
import numpy as np

L = 2
h_list = []
for Nx in [10, 20, 40, 80, 160]:
    Ny = Nx
    mesh = RectangleMesh(Point(-L / 2, -L / 2), Point(L / 2, L / 2), Nx, Ny)
    h = mesh.hmin()
    h_list.append(h)
    
np.savetxt('mesh_size.txt', h_list, delimiter=',')



