"""
This script is ussed to analyze the pulsatile pressure data used for aneurysm case. 
"""

import numpy as np
import matplotlib.pyplot as plt

# Read the data
data = np.loadtxt("p_t.csv", delimiter=",")
time = data[:,0]
pressure = data[:,1]

one_cardiac_cycle = 0.951   # in seconds
dt = time[1] - time[0]
n = int(one_cardiac_cycle/dt) # numer of time steps in one cardiac cycle
n_cycles = 6  # number of cardiac cycles

# Compute the mean and find maximum and minumum pressure in each cardiac cycle
mean_pressure = np.zeros(n_cycles)
max_pressure = np.zeros(n_cycles)
min_pressure = np.zeros(n_cycles)

mmHG_to_Pa = 133.322

for i in range(n_cycles):
    mean_pressure[i] = np.mean(pressure[i*n:(i+1)*n])
    print("Mean pressure in cycle %d is %f" % (i+1, mean_pressure[i]/mmHG_to_Pa))
    max_pressure[i] = np.max(pressure[i*n:(i+1)*n])
    print("Max pressure in cycle %d is %f" % (i+1, max_pressure[i]/mmHG_to_Pa))
    min_pressure[i] = np.min(pressure[i*n:(i+1)*n])
    print("Min pressure in cycle %d is %f" % (i+1, min_pressure[i]/mmHG_to_Pa))
    print("====================================")


plt.plot(time, pressure)
plt.show()