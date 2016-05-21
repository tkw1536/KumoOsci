from plotter import draw_networkx_graph
from graph_generators import cyclic_graph
import networkx as nx
import numpy as np
from matplotlib import pyplot as plt

def graph_from_matrix(A):
    """
    Creates a DiGraph from an adjacency matrix
    """
    
    A = np.array(A)
    N = A.shape[0]
    
    
    # make a graph
    G = nx.DiGraph()
    
    
    # add all the edges
    for i in range(N):
        for j in range(N):
            if A[i, j] != 0:
                G.add_edge(i, j, weight=A[i,j])
    
    # and return the graph
    return G

def layout_center(G, node, center = None):
    """ Makes a circular layout with node in the center """
    
    if center == None:
        center = [0, 0]
    
    # make a circular layout
    layout = nx.circular_layout(G)
    
    # re-center the nodes
    base = layout[node]
    for n in layout:
        l = layout[n]
        layout[n] = [l[0] - base[0] + center[0], l[1] - base[1] + center[1]]
    
    # return the layout
    return layout

def rename_nodes(G, f):
    """ Renames nodes using a function"""
    
    mapping = {}
    for n in G.nodes():
        mapping[n] = f(n)
    
    return nx.relabel_nodes(G, mapping)
    

def main():
    """ Main entry point """
    
    # make cyclic graphs
    G = graph_from_matrix(cyclic_graph(5))
    H = graph_from_matrix(cyclic_graph(3))
    
    # rename the nodes
    H = rename_nodes(H, lambda n:5+n)
    
    # anmd join them
    U = nx.compose(G, H)
    
    # make layouts
    layout = layout_center(G, 4)
    layout.update(layout_center(H, 6))
    
    # make colors
    colors = ['k' for i in range(8)]
    colors[3] = 'g'
    colors[6] = 'y'
    colors[5] = 'r'
    
    
    # plot the graph
    draw_networkx_graph(U, draw_labels = False, node_pos = layout, node_color = colors)
    plt.gca().set_xticklabels([])
    plt.gca().set_yticklabels([])  
    plt.show()
    

if __name__ == '__main__':
    main()