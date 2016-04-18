import matplotlib
matplotlib.use('Agg', force=True)
from matplotlib import pyplot as plt

import oscilator

import numpy as np
from numpy import random as npr
from graph_generators import cyclic_graph, complete_graph
from plotter import plot_network_and_graph, animate_network

def simulate_and_plot(A, omega):
    # create an oscilator object
    osc     =   oscilator.KuramotoOscilator(A = A, omegas = omega)
    
    # create initial values and time
    y0 = npr.uniform(0, 2*np.pi, size=osc.N)
    ts = np.arange(0, 50, 0.01)
    
    # simulate
    s = osc.simulate(y0, ts)
    
    # Make a new figure, plot and show
    plt.figure()
    ani = animate_network(osc, ts, s)
    ani.save('test.mp4', writer='imagemagick', fps=250, dpi=50)

def main():
    # set parameters and create oscilator
    A = - cyclic_graph(5)
    omega   =   0.3
    
    simulate_and_plot(A, omega)

if __name__ == '__main__':
    main()