import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def main():
    plt.rcParams['pdf.fonttype'] = 42
    plt.rcParams['ps.fonttype'] = 42
    plt.rcParams['font.family'] = 'Arial'
    plt.rcParams['font.size'] = 24
    plt.rcParams["figure.figsize"] = [10, 6]

    # Read the velocity waveform
    t_values, Q_ = np.loadtxt("MCA_10").T
    # Read the pressure waveform
    data = np.loadtxt("p_t.csv", delimiter=",")
    time = data[:,0]
    pressure = data[:,1]

    fig, ax = plt.subplots()
    ax.plot(t_values, Q_, color="black", linewidth=3, alpha=1, label = 'velocity')
    ax.set_xlabel("Time [s]", fontsize=22)
    ax.set_ylabel("Normalized velocity [-]", fontsize=22)
    ax.set_xlim(0, 0.951)
    ax.set_ylim(0, 2)
    ax.tick_params(axis='both', which='major', labelsize=22)
    ax2 = ax.twinx()
    ax2.plot(time, pressure/133.322, color="red", linewidth=3, alpha=1)
    ax.plot(np.nan, '-r', label = 'pressure', linewidth=3, alpha=1)  
    ax2.set_ylabel("Pressure [mmHg]", fontsize=22)
    ax2.tick_params(axis='both', which='major', labelsize=22)
    ax2.set_ylim(40, 150)
    ax.legend(loc='lower right', fontsize=20)
    # plt.savefig(Path.cwd() / "MCA_10.png", transparent=True, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    main()