import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def main():
    plt.rcParams['pdf.fonttype'] = 42
    plt.rcParams['ps.fonttype'] = 42
    plt.rcParams['font.family'] = 'Arial'
    plt.rcParams['font.size'] = 24
    plt.rcParams["figure.figsize"] = [10, 6]
    t_values, Q_ = np.loadtxt("MCA_10").T


    plt.plot(t_values, Q_, color="black", linewidth=1.5, alpha=1)
    # probe_point = [100, 140, 200, 300, 420, 600]
    # for i in probe_point:
    #     plt.scatter(t_values[i],Q_[i], color="blue", s=40)
    plt.xlabel("Time [s]", fontsize=22)
    plt.ylabel("Normalized velocity [-]", fontsize=22)
    plt.xlim(0, 0.951)
    plt.tick_params(axis='both', which='major', labelsize=22)
    plt.savefig(Path.cwd() / "MCA.png", transparent=True, bbox_inches='tight')
    # plt.show()

if __name__ == "__main__":
    main()