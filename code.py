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
    
    # first plot the graph itself
    plt.subplot(212)
    colors = []
    
    for j in range(osc.N):
        # draw and store color
        c = plt.plot(ts, s[:,j], label='Oscilator %s' % (j))
        colors.append(c[0].get_color())
    
    # now plot the graph
    plt.subplot(211)
    
    # Get the graph and layout
    G = osc.graph
    layout = nx.circular_layout(G)
    
    # draw each of the components with the right color
    nx.draw_networkx_edges(G, pos=layout)
    nx.draw_networkx_nodes(G, pos=layout, node_color=colors)
    nx.draw_networkx_labels(G, pos=layout)
    
    # and show it
    plt.show()

def main():
    # set parameters and create oscilator
    A = - cyclic_graph(3)
    omega   =   0.3
    
    simulate_and_plot(A, omega)

if __name__ == '__main__':
    main()