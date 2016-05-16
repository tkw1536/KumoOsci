import numpy as np

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
    