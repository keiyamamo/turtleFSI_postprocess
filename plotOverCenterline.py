import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from argparse import ArgumentParser

from scipy.signal import argrelextrema

plt.rcParams['font.family'] ='sans-serif'
plt.rcParams['font.size'] = 14
plt.rcParams["figure.figsize"] = [8, 6]
plt.rcParams['axes.linewidth'] = 1


parser = ArgumentParser()

parser.add_argument("--case0", type=str, metavar="PATH", help="path to csv file")
parser.add_argument("--case1", type=str, metavar="PATH", help="path to coilT2")
parser.add_argument("--case2", type=str, metavar="PATH", help="path to coilT3")

args = parser.parse_args()

# case0 = args.case0
# case1 = args.case1
# case = args.case2

def plotOverCenterline(path_to_case):
    coil_data = pd.read_csv(path_to_case)
    coil_data_np_array = coil_data.to_numpy()
    abscissas = coil_data_np_array[:,1]
    mydata = coil_data_np_array[:,2]
  
    return abscissas, mydata

fig, ax = plt.subplots()

if args.case0:
    c1_abscissas, c1_data = plotOverCenterline(args.case0)
    ax.plot(c1_abscissas, c1_data/c1_data[-1], label="c1", color="k")
    # ax.annotate("coilT1", xy=(29.5, 0.0048)) # for tke
    
if args.case1:
    c2_abscissas, c2_data = plotOverCenterline(args.case1)
    ax.plot(c2_abscissas, c2_data/c2_data[-1], label="c2",color="b")
    # ax.annotate("coilT2", xy=(46.3, 0.0013), color="b") # for tke
    
if args.case2:
    c3_abscissas, c3_data = plotOverCenterline(args.case2)
    ax.plot(c3_abscissas, c3_data/c3_data[-1], label="c3" ,color="r")
    # ax.annotate("coilT3", xy=(63.6, 0.0009), color="r") # for tke

ax.set_xlabel("Abscissas", fontsize=16) 
ax.set_ylabel("Kinetic Energy", fontsize=16)
ax.set_xlim(0, 70)
ax.tick_params(which='both', direction='in',bottom=True, top=True, left=True, right=True)
# plt.savefig("/Users/k eiyamamoto/Desktop/kineticEnergy.png", transparent=True)
# plt.legend(fontsize=16)
plt.show()