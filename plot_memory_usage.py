import argparse
import numpy as np
import matplotlib.pyplot as plt

def command_line_parser():
    parser = argparse.ArgumentParser(description="Read a text file")
    parser.add_argument("filename", help="Name of the text file")
    return parser

def read_plot_txt(filename):
    data = np.loadtxt(filename)
    t = np.linspace(0, len(data), len(data))
    start = 1
    stop = len(data)
    plt.rcParams["figure.figsize"] = [14, 6]
    plt.plot(t[start:stop], data[start:stop])
    plt.xlabel("Time step")
    plt.ylabel("Memory usage (MB)")
    plt.show()


if __name__ == "__main__":
    parser = command_line_parser()
    args = parser.parse_args()
    read_plot_txt(args.filename)
    


