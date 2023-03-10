"""
Given txt file that constains the error of the solution at each configuration,
this script will first comput the convergence rate of the solution, anf then
generate a plot of the error vs. the mesh size or time step size using log scale.
"""

import numpy as np
import matplotlib.pyplot as plt
import sys



def compute_convergence_rate(error_v, error_p, mesh_size, type='space'):
    """
    Compute the convergence rate of the solution
    """
    # Compute the convergence rate against the mesh size or time step size
    convergence_rate_v = np.zeros(error_v.shape[0])
    convergence_rate_p = np.zeros(error_p.shape[0])
    
    # create time step array starting from 0.5 and halving each time
    time_step_size = np.zeros(error_v.shape[0])
    time_step_size[0] = 0.5
    # compute convergence rate for the velocity 
    for i in range(1, error_v.shape[0]):
        if type =='space':
            convergence_rate_v[i] = np.log(error_v[i-1]/error_v[i])/np.log(mesh_size[i-1]/mesh_size[i])
        elif type == 'time':
            time_step_size[i] = time_step_size[i-1]/2
            convergence_rate_v[i] = np.log(error_v[i-1]/error_v[i])/np.log(time_step_size[i-1]/time_step_size[i])
    
    # compute convergence rate for the pressure
    for i in range(1, error_p.shape[0]):
        if type =='space':
            convergence_rate_p[i] = np.log(error_p[i-1]/error_p[i])/np.log(mesh_size[i-1]/mesh_size[i])
        elif type == 'time':
            convergence_rate_p[i] = np.log(error_p[i-1]/error_p[i])/np.log(time_step_size[i-1]/time_step_size[i])

    return convergence_rate_v, convergence_rate_p, time_step_size

def plot_convergence_rate(error_v, error_p, mesh_size, convergence_rate_v, convergence_rate_p, time_step_size, type='space'):
    """
    Plot the error vs. the mesh size using log scale
    """
    label_format = '{:.0e}'
    x_tick_list = [1e-2, 1e-1, 4e-1]
    if type=='space':
        # Plot the error vs. the mesh size using log scale
        fig, ax = plt.subplots()
        ax.loglog(mesh_size, error_v, 'o-', color="blue", label='Velocity')
        ax.grid(True, which="both", ls="-", alpha=0.5)
        ax.set_xlabel('Mesh size')
        ax.set_xticks(x_tick_list)
        ax.set_xticklabels(label_format.format(x) for x in x_tick_list)
        ax.set_ylabel('Error')
        ax.set_xlim([min(x_tick_list), max(x_tick_list)])

        for xi, yi, text in zip(mesh_size, error_v, convergence_rate_v):
            if text != 0:
                text = np.around(text, decimals=2)
                ax.annotate(text,
                            xy=(xi, yi), xycoords='data', color='blue',
                            xytext=(25, 7), textcoords='offset points')
        ax.loglog(mesh_size, error_p, 'o-', color="red", label='Pressure')
        for xi, yi, text in zip(mesh_size, error_p, convergence_rate_p):
            if text != 0:
                text = np.around(text, decimals=2)
                ax.annotate(text,
                            xy=(xi, yi), xycoords='data', color='red',
                            xytext=(20, 17), textcoords='offset points')
        plt.title("Spatial convergence of the error with P2P1 elements")
        plt.legend(['Velocity', 'Pressure'], loc="lower right")
        plt.savefig("spatial_convergence.png")
        plt.close()

    # Plot the convergence rate vs. the mesh size using log scale
    elif type=='time':
        # Plot the error vs. the time step size using log scale
        plt.figure()
        plt.loglog(time_step_size, error_v, 'o-')
        plt.grid(True, which="both", ls="-")
        plt.xlabel('Time step size')
        plt.ylabel('Error')
        plt.title("Temporal convergence of the error")
        plt.savefig("temporal_convergence.png")
        plt.close()
   
def main():
    # Read the error from the txt file
    error_v = np.loadtxt(sys.argv[1])
    error_p = np.loadtxt(sys.argv[2])
    mesh_size = np.loadtxt(sys.argv[3])
    type = 'space'
    # Compute the convergence rate
    convergence_rate_v, convergence_rate_p, time_step_size = compute_convergence_rate(error_v, error_p, mesh_size, type)
    # Plot the error vs. the mesh size using log scale
    plot_convergence_rate(error_v, error_p, mesh_size, convergence_rate_v, convergence_rate_p, time_step_size, type)

if __name__ == '__main__':
    main()
    