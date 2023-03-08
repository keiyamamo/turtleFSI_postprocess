"""
This script is ussed to analyze the pulsatile pressure data used for aneurysm case. 
"""

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
# Read the data
data = np.loadtxt("FC_pressure_flow/p_t.csv", delimiter=",")
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
ax.set_xlabel("Time [s]", fontsize=18)
ax.set_ylabel("Pressure [mmHg]", fontsize=18)
ax.plot(time, pressure/mmHG_to_Pa, color="black", linewidth=2, alpha=1, label = 'Normal')

data = np.loadtxt("FC_pressure_flow/p_t_min100_max170mmHg.csv", delimiter=",")
time = data[:,0]
pressure = data[:,1]
ax.plot(time, pressure/mmHG_to_Pa, color="red", linewidth=2, alpha=1, label = 'High')
# ax.legend(loc='upper right', fontsize=14)
plt.show()