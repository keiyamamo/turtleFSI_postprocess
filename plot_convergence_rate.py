"""
Given txt file that constains the error of the solution at each configuration,
this script will first comput the convergence rate of the solution, anf then
generate a plot of the error vs. the mesh size using log scale.
"""

import numpy as np
import matplotlib.pyplot as plt
import sys

def compute_convergence_rate(error, mesh_size):
    """
    Compute the convergence rate of the solution
    """
    # Compute the convergence rate
    convergence_rate = np.zeros(error.shape[0])
    for i in range(1, error.shape[0]):
        convergence_rate[i] = np.log(error[i-1]/error[i])/np.log(mesh_size[i-1]/mesh_size[i])
    return convergence_rate

def plot_convergence_rate(error, mesh_size, convergence_rate, title, filename):
    """
    Plot the error vs. the mesh size using log scale
    """
    # Plot the error vs. the mesh size using log scale
    plt.figure()
    plt.loglog(mesh_size, error, 'o-')
    plt.xlabel('Mesh size')
    plt.ylabel('Error')
    plt.title(title)
    plt.savefig(filename)
    plt.close()

    # Plot the convergence rate vs. the mesh size using log scale
    plt.figure()
    plt.loglog(mesh_size, convergence_rate, 'o-')
    plt.xlabel('Mesh size')
    plt.ylabel('Convergence rate')
    plt.title(title)
    plt.savefig(filename[:-4]+'_convergence_rate.png')
    plt.close()

def main():
    # Read the error from the txt file
    error = np.loadtxt(sys.argv[1])
    mesh_size = np.loadtxt(sys.argv[2])

    # Compute the convergence rate
    convergence_rate = compute_convergence_rate(error, mesh_size)

    # Plot the error vs. the mesh size using log scale
    plot_convergence_rate(error, mesh_size, convergence_rate, 'Convergence rate of the solution', 'convergence_rate.png')

if __name__ == '__main__':
    main()
    