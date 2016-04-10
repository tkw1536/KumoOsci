import numpy as np
from scipy.integrate import odeint

class KuramotoOscilator(object):
    """
    Represents an oscilator class
    """
    def __init__(self, A, omegas, B = 0, OMEGA = 0):
        """
        Creates a new oscilator. 
        
        Arguments:
            A
                matrix of shape N x N containing binding coeffcients
                between the oscilators
            omegas
                A vector of length N or a scalar representing the frequence of
                the system. In case of a scalar, will automatically convert to a
                vector. 
            B
                A vector of length N or a scalar representing the binding 
                coefficients between the external driver and the system. In case
                of a scalar, will automatically convert to a vector. 
            OMEGA
                Optional. A scalar OMEGA that will be used to drive the system. 
        """
        
        # store A
        self._A = np.array(A)
        
        # extract the size
        self._N = self._A.shape[0]
        
        # check that A is square 
        if self._A.shape != (self._N, self._N):
            raise ValueError('matrix A is not square')
        
        # if we have a scalar as an omega, we scale up
        if np.isscalar(omegas):
            self._omegas = omegas * np.ones(self._N)
        
        # else we verify that we have the right shape
        else:
            self._omegas = np.array(omegas)
            
            if self._omegas.shape != (self._N, ):
                raise ValueError('omegas needs to be a scalar or vector of length N')
        
        # if we have a scalar as an omega, we scale up
        if np.isscalar(B):
            self._B = B * np.ones(self._N)
        
        # else we verify that we have the right shape
        else:
            self._B = np.array(B)
            
            if self._B.shape != (self._N, ):
                raise ValueError('B needs to be a scalar or vector of length N')
        
        # OMEGA (needs to be scalar)
        if np.isscalar(OMEGA):
            self._OMEGA = OMEGA
        else:
            raise ValueError('OMEGA needs to be a scalar')
        
    #
    # PROPERTIES - get the matrices etc back
    #
    @property
    def A(self):
        """
        Returns the matrix A of this system
        """
        return self._A
    
    @property
    def N(self):
        """
        Returns the size N of this system
        """
        return self._N
    
    @property
    def omegas(self):
        """
        Returns the vector of omegas of this system
        """
        return self._omegas
    
    @property
    def B(self):
        """
        Returns the vector B of this system
        """
        return self._B
    
    @property
    def OMEGA(self):
        """
        Returns the vector OMEGA of this system
        """
        return self._OMEGA
    #
    # BUILDING differential equation
    #
    def to_equation(self):
        """
        Creates a function theta'(theta, t) representing the system
        
        Returns:
            a lambda function with the given parameters
        """
        
        return eval(self.to_equation_str())
    
    def to_equation_str(self):
        """
        Returns a string representing the ode describing this system
        """
        
        # we need to do it seperatly for each part of the ode
        ode_parts = []
        
        for i, o in enumerate(self.omegas):
            # omega
            s = ['%s' % o]
            
            for j in range(self.N):
                if (self.A[i, j] != 0) and (i != j):
                    # A[i,j]*sin(theta[j] - theta[i])
                    s.append('(%s)*np.sin(theta[%s] - theta[%s])' % (self.A[i, j], j, i))
            
            if self.B[i] != 0:
                # B[i] * np.sin(Phi(t) - theta[i])
                s.append(
                    '(%s)*np.sin((%s)*t - theta[%s])' % (self.B[i], self.OMEGA, i)
                )
            
            # join them as a sum
            ode_parts.append('(%s)' % ')+('.join(s))
        
        print(ode_parts)
        
        # build a function string
        return 'lambda theta,t:np.array([(%s)])' % '),('.join(ode_parts)
    
    def simulate(self, y0, t, *args, **kwargs):
        """
        Shortcut for scipy.integrate.odeint(self.to_equation(), y0, t, *args, *kwargs)
        """
        
        # solve the system
        sol = odeint(self.to_equation(), y0, t, *args, **kwargs)
        
        # make sure we go from 0 to 2*pi
        sol %= 2*np.pi
        
        # return solution
        return sol
    
    def simulate_and_plot(self, y0, t, *args, **kwargs):
        """
        Simulates this system and then plots it
        """
        
        import matplotlib.pyplot as plt
        
        # simulate the solution
        sol = self.simulate(y0, t, *args, **kwargs)
        
        # plot all the solutions in dependencies of time
        for i in range(self.N):
            plt.plot(t, sol[:, i])
        
        # and show the plot
        plt.show()