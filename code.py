import oscilator

import numpy as np
from numpy import random as npr

from matplotlib import pyplot as plt

from tqdm import trange

def main():
    
    # set parameters and create oscilator
    A = [
        [0, -1, -1], 
        [-1, 0, -1], 
        [-1, -1, 0]
    ]
    omega   =   0.3
    osc     =   oscilator.KuramotoOscilator(A = A, omegas = omega)
    
    # number of times we smulate, 100 for now
    N = 1
    
    # creat initial values and time
    y0s = npr.uniform(0, 2*np.pi, size=(N, osc.N))
    ts = np.arange(0, 20, 0.01)
    
    # solutions
    sols = []
    
    # repeat N times
    for i in trange(N):
        s = osc.simulate(y0s[i], ts)
        sols.append(s)
        
        for j in range(osc.N):
            plt.plot(ts, s[:,j], label='Run %s Iterator %s' % (i, j))
    
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()