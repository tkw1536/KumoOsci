import oscilator

import numpy as np
from numpy import random as npr
from graph_generators import cyclic_graph, complete_graph

from matplotlib import pyplot as plt

import networkx as nx

def simulate_and_plot(A, omega):
    # create an oscilator object
    osc     =   oscilator.KuramotoOscilator(A = A, omegas = omega)
    
    # create initial values and time
    y0 = npr.uniform(0, 2*np.pi, size=osc.N)
    ts = np.arange(0, 20, 0.01)
    
    # simulate
    s = osc.simulate(y0, ts)
    
    # make a new figure and subplot
    plt.figure()
    
    # plot the graph
    plt.subplot(211)
    nx.draw_networkx(osc.graph)
    
    # plot the graph itself
    plt.subplot(212)
    
    for j in range(osc.N):
        plt.plot(ts, s[:,j], label='Oscilator %s' % (j))
    
    # add a legend
    #plt.legend()
    
    # and show it
    plt.show()

def main():
    # set parameters and create oscilator
    A = - cyclic_graph(8)
    omega   =   0.3
    
    simulate_and_plot(A, omega)

if __name__ == '__main__':
    main()