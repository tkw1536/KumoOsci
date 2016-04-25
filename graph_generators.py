import numpy as np
from numpy import random as npr

def cyclic_graph(N):
    """
    Creates the adjacency matrix of a cyclic graph. 
    
    Arguments:
        N
            Size of the cyclic graph
    """
    
    # start with a matrix of zeros
    A = np.zeros((N, N))
    
    # connect _ -> _ + 1
    i = np.arange(N)
    j = (i + 1) % N
    
    # set the indexes
    A[i,j] = 1
    A[j,i] = 1
    
    # return A
    return A
    
def complete_graph(N):
    """
    Creates the adjacency matrix of a complete graph. 
    
    Arguments:
        N
            Size of the complete graph
    """
    
    return np.ones((N, N)) - np.eye(N)

def random_graph(N):
    """
    Creates the adjacency matrix of a random graph. 
    
    Arguments:
        N
            Size of the random graph. 
    """
    
    A = np.zeros((N, N))
    
    for i in range(N):
        for j in range(i):
            A[i, j] = npr.randint(2)
            A[j, i] = A[i, j]
    
    return A