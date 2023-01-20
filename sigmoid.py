import  numpy as np
import  matplotlib.pyplot as plt


# create a sigmoid function
def sigmoid ():
    num_step_for_cardiac_cycle = 2800
    num_ramp = 800
    dt = 0.00033964286
    t_ramp = num_ramp*dt
    t = np.linspace(0, t_ramp, num_ramp)
    # create sigmoid function
    sigmoid = 1 / (1 + np.exp(-10*(t/t_ramp-0.5)))
    plt.plot(t, sigmoid)
    plt.show()

if __name__ == "__main__":
    sigmoid()
    