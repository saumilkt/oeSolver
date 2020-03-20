# OE Infection modeling
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
plt.ion()
plt.rcParams['figure.figsize'] = 10, 8

a = 50.000  # birth rate
bi = 0.8000  # Desity-independent death percent (per day)
bd = 0.1000  # Desity-dependent death percent  (per day)
I = .01*N0  # resurect percent (per day)
v = .9000  # rate of maternal transmission
alpha_i = 0.2 # pre-adult virulence
alpha_a = 0.1 # adult virulence 


# solve the system dy/dt = f(y, t)
def f(N, t):
     Ni = N[0]
     # the model equations (see Munz et al. 2009)
     f0 = Ni*(a-bi-bd*Ni)-I*((1+a*(v*alpha_i-1))+alpha_a)
     return [f0]

# initial conditions
N0 = 500.              # initial population
y0 = [N0]     # initial condition vector
t  = np.linspace(0, 5., 1000)         # time grid

# solve the DEs
soln = odeint(f, y0, t)
S = soln[:, 0]

# plot results
plt.figure()
plt.plot(t, S, label='Living')
plt.xlabel('Timesteps')
plt.ylabel('Population')
plt.title('OE Infestation - No Init. Dead Pop.; No New Births.')
plt.legend(loc=0)
